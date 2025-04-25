Software Development Agent
The Software Development Agent is an AI-powered web application that streamlines software development by generating project requirements, system designs, code, test cases, code reviews, and documentation. Built with Flask, LangGraph, and the Grok LLM (via LangChain-Groq), it provides a user-friendly interface to input project prompts and view AI-generated outputs in real time. Developed by Nabafat.AI, this tool is ideal for developers, startups, and educators looking to accelerate prototyping and learning.
Features

Multi-Stage Workflow: Generates six stages of software development:
Requirement Clarification
System Design
Code Generation (rendered as markdown)
Test Case Generation (syntax-highlighted Python)
Code Review with security feedback
Documentation


Real-Time Streaming: Outputs stream stage-by-stage using Server-Sent Events (SSE).
Editable Outputs: Edit and regenerate individual stage outputs with a user-friendly interface.
Prompt History: Stores and recalls recent prompts via a dropdown.
Dark Mode: Toggle between light and dark themes for better accessibility.
Downloadable Outputs: Export all outputs as a ZIP file.
Security Feedback: Automatically scans generated code for common vulnerabilities (e.g., eval(), hardcoded secrets).
Responsive UI: Built with Tailwind CSS, featuring a teal, coral, and dark gray theme with a green "Generate" button.

Prerequisites

Python: 3.8 or higher
Git: For cloning and version control
Groq API Key: Obtain from Groq for LLM access
Node.js: Optional, for local development with Tailwind CSS (if modifying frontend)

Installation

Clone the Repository:
git clone https://github.com/abdull6771/software-development-agent.git
cd software-development-agent


Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Configure Environment Variables: Create a .env file in the project root:
echo "GROQ_API_KEY=your-groq-api-key" > .env


Run the Application:
python app.py

Open http://localhost:5000 in your browser.


Usage

Enter a Prompt:

In the input field, type a project idea (e.g., “Build a Flask API for user management with RBAC”).
Use the prompt history dropdown to recall recent prompts.


Generate Outputs:

Click the green “Generate” button to start the AI workflow.
Watch outputs stream in real time across six stages, with accordions expanding automatically.


Interact with Outputs:

Edit: Click “Edit” to modify any stage’s content (e.g., tweak generated code).
Regenerate: Click “Regenerate” to re-run a specific stage with updated input.
Copy: Use “Copy to Clipboard” to extract content.
Download: Click “Download Outputs” to save all stages as a ZIP file.


Toggle Themes:

Click the sun/moon icon in the header to switch between light and dark modes.


Review Security Feedback:

Check the Code Review stage for warnings about potential vulnerabilities in the generated code.



Project Structure
software-development-agent/
├── app.py                    # Flask backend with LangGraph workflow
├── templates/
│   └── index.html            # Frontend with Tailwind CSS and JavaScript
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not tracked)
└── README.md                 # This file

Dependencies
Key dependencies listed in requirements.txt:

flask==1.1.2
langgraph==0.2.3
langchain-groq==0.2.0
langchain-core==0.3.8

For a full list, see requirements.txt.
Contributing
We welcome contributions to enhance the Software Development Agent! To contribute:

Fork the Repository:
git fork https://github.com/abdull6771/software-development-agent.git


Create a Feature Branch:
git checkout -b feature/your-feature


Commit Changes:
git commit -m "Add your feature"


Push and Create a Pull Request:
git push origin feature/your-feature

Open a pull request on GitHub with a clear description of your changes.


Please follow our Code of Conduct and ensure your code adheres to PEP 8 standards.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions, suggestions, or collaboration, reach out to Nabafat.AI or open an issue on this repository.

Built with ❤️ by Nabafat.AI. Star this repo if you find it useful!
