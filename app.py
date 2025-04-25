from flask import Flask, render_template, request, jsonify
from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from typing import TypedDict
import os

app = Flask(__name__)
os.environ["GROQ_API_KEY"] = ""

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# State type definition
class SoftwareDevState(TypedDict):
    user_prompt: str
    clarified_requirements: str
    system_design: str
    source_code: str
    test_cases: str
    review_comments: str
    documentation: str

# Agent Definitions
def requirement_agent(state: SoftwareDevState):
    prompt = ChatPromptTemplate.from_template(
        """You are a software project manager. Clarify the following user request into structured, complete technical requirements.
        User Request: {user_prompt}"""
    )
    chain = prompt | llm
    clarified = chain.invoke({"user_prompt": state["user_prompt"]}).content
    return {"clarified_requirements": clarified}

def design_agent(state: SoftwareDevState):
    prompt = ChatPromptTemplate.from_template(
        """You are a senior software architect. Design the architecture and suggest tech stack based on:
        Requirements: {clarified_requirements}"""
    )
    chain = prompt | llm
    design = chain.invoke({"clarified_requirements": state["clarified_requirements"]}).content
    return {"system_design": design}

def code_agent(state: SoftwareDevState):
    prompt = ChatPromptTemplate.from_template(
        """You are a software engineer. Generate clean, modular, production-ready code based on this design:
        Design: {system_design}"""
    )
    chain = prompt | llm
    code = chain.invoke({"system_design": state["system_design"]}).content
    return {"source_code": code}

def test_agent(state: SoftwareDevState):
    prompt = ChatPromptTemplate.from_template(
        """You are a QA engineer. Write unit and integration tests for the following code:
        Code: {source_code}"""
    )
    chain = prompt | llm
    tests = chain.invoke({"source_code": state["source_code"]}).content
    return {"test_cases": tests}

def review_agent(state: SoftwareDevState):
    prompt = ChatPromptTemplate.from_template(
        """You are a senior developer reviewing this code. Provide constructive comments and highlight improvements.
        Code: {source_code}"""
    )
    chain = prompt | llm
    review = chain.invoke({"source_code": state["source_code"]}).content
    return {"review_comments": review}

def doc_agent(state: SoftwareDevState):
    prompt = ChatPromptTemplate.from_template(
        """You are a technical writer. Generate README content and API documentation for the following project.
        Requirements: {clarified_requirements}
        Code: {source_code}"""
    )
    chain = prompt | llm
    docs = chain.invoke({"clarified_requirements": state["clarified_requirements"], "source_code": state["source_code"]}).content
    return {"documentation": docs}

# LangGraph Setup
graph = StateGraph(SoftwareDevState)
graph.add_node("clarify", requirement_agent)
graph.add_node("design", design_agent)
graph.add_node("code", code_agent)
graph.add_node("test", test_agent)
graph.add_node("review", review_agent)
graph.add_node("document", doc_agent)

graph.set_entry_point("clarify")
graph.add_edge("clarify", "design")
graph.add_edge("design", "code")
graph.add_edge("code", "test")
graph.add_edge("test", "review")
graph.add_edge("review", "document")
graph.add_edge("document", END)

workflow = graph.compile()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_prompt = data.get('user_prompt')
    if not user_prompt:
        return jsonify({'message': 'Prompt is required'}), 400
    try:
        result = workflow.invoke({"user_prompt": user_prompt})
        return jsonify(result)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)