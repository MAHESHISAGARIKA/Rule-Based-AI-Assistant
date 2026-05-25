"""
Knowledge base for Rule Based AI Assistant.

This file contains predefined rules, patterns, and responses.
The assistant does not use machine learning. It uses rule-based matching.
"""

KNOWLEDGE_BASE = {
    "greeting": {
        "patterns": [
            "hi", "hello", "hey", "hai", "good morning", "good afternoon",
            "good evening", "start", "yo"
        ],
        "response": "Hello! I am Rule Based AI Assistant. How can I help today?"
    },

    "how_are_you": {
        "patterns": [
            "how are you", "how are you doing", "are you ok", "how is it going"
        ],
        "response": "I am working perfectly. Thank you for asking!"
    },

    "assistant_name": {
        "patterns": [
            "what is your name", "your name", "who are you", "tell me your name"
        ],
        "response": "My name is Rule Based AI Assistant. I am a simple chatbot built using predefined rules."
    },

    "creator": {
        "patterns": [
            "who created you", "who made you", "who developed you",
            "your developer", "who is your developer"
        ],
        "response": "I was developed as an internship project to demonstrate rule-based AI logic."
    },

    "project_explanation": {
        "patterns": [
            "what is this project", "explain this project", "project idea",
            "about this project", "tell me about project"
        ],
        "response": (
            "This project is called Rule Based AI Assistant. It responds to user messages "
            "using predefined rules, input cleaning, pattern matching, fallback responses, "
            "and exit commands."
        )
    },

    "project_features": {
        "patterns": [
            "features", "project features", "what are the features",
            "features of this chatbot", "what can this project do"
        ],
        "response": (
            "Main features include greeting handling, predefined question answering, "
            "input sanitization, dictionary-based matching, fallback response, exit command, "
            "CLI interface, and Flask web interface."
        )
    },

    "project_goal": {
        "patterns": [
            "project goal", "goal of this project", "aim of this project",
            "purpose of this project"
        ],
        "response": (
            "The goal of this project is to understand basic AI logic using control flow, "
            "decision-making, loops, and rule-based response generation."
        )
    },

    "what_can_you_do": {
        "patterns": [
            "what can you do", "help", "commands", "show commands",
            "how can you help", "available commands"
        ],
        "response": (
            "I can answer questions about AI, rule-based chatbots, Python, Git, GitHub, "
            "VS Code, Flask, web development, and this internship project. Try asking: "
            "'what is ai', 'what is python', 'what is github', or 'project features'."
        )
    },

    "ai_definition": {
        "patterns": [
            "what is ai", "what is artificial intelligence", "define ai",
            "explain ai", "ai meaning", "artificial intelligence"
        ],
        "response": (
            "Artificial Intelligence is the ability of a computer system to perform tasks "
            "that normally require human intelligence, such as reasoning, decision-making, "
            "learning, and answering questions."
        )
    },

    "ai_examples": {
        "patterns": [
            "examples of ai", "ai examples", "where ai is used",
            "applications of ai", "uses of artificial intelligence"
        ],
        "response": (
            "AI is used in chatbots, recommendation systems, voice assistants, image recognition, "
            "medical diagnosis, fraud detection, self-driving vehicles, and smart search engines."
        )
    },

    "machine_learning": {
        "patterns": [
            "what is machine learning", "define machine learning", "explain machine learning",
            "ml meaning", "what is ml"
        ],
        "response": (
            "Machine Learning is a branch of AI where systems learn patterns from data "
            "instead of being programmed with only fixed rules."
        )
    },

    "deep_learning": {
        "patterns": [
            "what is deep learning", "define deep learning", "explain deep learning",
            "dl meaning"
        ],
        "response": (
            "Deep Learning is a type of machine learning that uses neural networks with many layers "
            "to learn complex patterns from large amounts of data."
        )
    },

    "rule_based_ai": {
        "patterns": [
            "what is rule based ai", "what is rule based chatbot",
            "explain rule based chatbot", "how rule based chatbot works",
            "rule based ai meaning"
        ],
        "response": (
            "Rule-based AI works using predefined rules. The system checks the user input "
            "and selects a response based on fixed patterns or conditions."
        )
    },

    "rule_based_vs_ai": {
        "patterns": [
            "difference between rule based and machine learning",
            "rule based vs machine learning",
            "rule based ai vs ml",
            "rule based chatbot vs ai chatbot"
        ],
        "response": (
            "A rule-based system follows fixed rules written by developers. "
            "A machine learning system learns patterns from data and can improve through training."
        )
    },

    "chatbot_definition": {
        "patterns": [
            "what is chatbot", "define chatbot", "explain chatbot",
            "chatbot meaning"
        ],
        "response": (
            "A chatbot is a software application that communicates with users through text or voice."
        )
    },

    "input_sanitization": {
        "patterns": [
            "what is input sanitization", "explain input sanitization",
            "why clean input", "input cleaning"
        ],
        "response": (
            "Input sanitization means cleaning user input before processing. "
            "For example, converting text to lowercase and removing extra spaces."
        )
    },

    "fallback_response": {
        "patterns": [
            "what is fallback", "what is fallback response",
            "explain fallback response", "default response"
        ],
        "response": (
            "A fallback response is the default reply given when the assistant does not understand "
            "the user's message."
        )
    },

    "python_definition": {
        "patterns": [
            "what is python", "define python", "explain python",
            "python meaning", "python"
        ],
        "response": (
            "Python is a beginner-friendly programming language used for web development, "
            "automation, data analysis, AI, and machine learning."
        )
    },

    "python_uses": {
        "patterns": [
            "uses of python", "where python is used", "python applications",
            "why use python"
        ],
        "response": (
            "Python is used in AI, machine learning, web development, automation, data science, "
            "scripting, testing, and software development."
        )
    },

    "variable": {
        "patterns": [
            "what is variable", "define variable", "explain variable"
        ],
        "response": (
            "A variable is a named storage location used to store data in a program."
        )
    },

    "function": {
        "patterns": [
            "what is function", "define function", "explain function",
            "function in python"
        ],
        "response": (
            "A function is a reusable block of code that performs a specific task."
        )
    },

    "loop": {
        "patterns": [
            "what is loop", "define loop", "explain loop",
            "while loop", "for loop"
        ],
        "response": (
            "A loop is used to repeat a block of code multiple times. "
            "Common loops are for loop and while loop."
        )
    },

    "if_else": {
        "patterns": [
            "what is if else", "explain if else", "if else meaning",
            "conditional statement"
        ],
        "response": (
            "If-else is a decision-making structure. It runs different code depending on whether "
            "a condition is true or false."
        )
    },

    "dictionary": {
        "patterns": [
            "what is dictionary", "dictionary in python", "explain dictionary",
            "hash map", "key value pair"
        ],
        "response": (
            "A dictionary in Python stores data as key-value pairs. It is useful for fast lookup, "
            "such as matching user questions to chatbot responses."
        )
    },

    "flask": {
        "patterns": [
            "what is flask", "explain flask", "flask framework",
            "why use flask"
        ],
        "response": (
            "Flask is a lightweight Python web framework used to build web applications and APIs."
        )
    },

    "html": {
        "patterns": [
            "what is html", "define html", "explain html", "html meaning"
        ],
        "response": (
            "HTML stands for HyperText Markup Language. It is used to structure web pages."
        )
    },

    "css": {
        "patterns": [
            "what is css", "define css", "explain css", "css meaning"
        ],
        "response": (
            "CSS stands for Cascading Style Sheets. It is used to style web pages with colors, "
            "layouts, fonts, and spacing."
        )
    },

    "javascript": {
        "patterns": [
            "what is javascript", "define javascript", "explain javascript",
            "js meaning"
        ],
        "response": (
            "JavaScript is a programming language used to make web pages interactive."
        )
    },

    "frontend": {
        "patterns": [
            "what is frontend", "frontend meaning", "explain frontend"
        ],
        "response": (
            "Frontend is the part of a website or application that users see and interact with."
        )
    },

    "backend": {
        "patterns": [
            "what is backend", "backend meaning", "explain backend"
        ],
        "response": (
            "Backend is the server-side part of an application. It handles logic, data processing, "
            "databases, and APIs."
        )
    },

    "api": {
        "patterns": [
            "what is api", "api meaning", "explain api",
            "application programming interface"
        ],
        "response": (
            "API stands for Application Programming Interface. It allows different software systems "
            "to communicate with each other."
        )
    },

    "git": {
        "patterns": [
            "what is git", "define git", "explain git", "git meaning"
        ],
        "response": (
            "Git is a version control system that helps developers track code changes and manage "
            "project history."
        )
    },

    "github": {
        "patterns": [
            "what is github", "define github", "explain github",
            "github meaning"
        ],
        "response": (
            "GitHub is an online platform used to store, manage, share, and collaborate on code "
            "projects using Git."
        )
    },

    "repository": {
        "patterns": [
            "what is repository", "repo meaning", "github repository",
            "what is repo"
        ],
        "response": (
            "A repository is a project storage location that contains code files, folders, "
            "documentation, and version history."
        )
    },

    "commit": {
        "patterns": [
            "what is commit", "git commit meaning", "explain commit"
        ],
        "response": (
            "A commit is a saved snapshot of project changes in Git."
        )
    },

    "push": {
        "patterns": [
            "what is push", "git push meaning", "explain push",
            "push to github"
        ],
        "response": (
            "Git push uploads local code changes from the computer to a remote repository such as GitHub."
        )
    },

    "pull": {
        "patterns": [
            "what is pull", "git pull meaning", "explain pull"
        ],
        "response": (
            "Git pull downloads the latest changes from a remote repository to the local computer."
        )
    },

    "branch": {
        "patterns": [
            "what is branch", "git branch meaning", "explain branch"
        ],
        "response": (
            "A branch is a separate version of a project where developers can work without affecting "
            "the main code."
        )
    },

    "vs_code": {
        "patterns": [
            "what is vs code", "what is visual studio code",
            "explain vs code", "vs code meaning"
        ],
        "response": (
            "VS Code is a popular code editor used to write, run, debug, and manage code projects."
        )
    },

    "terminal": {
        "patterns": [
            "what is terminal", "explain terminal", "command line",
            "what is command prompt"
        ],
        "response": (
            "A terminal is a command-line tool used to run commands, start programs, install packages, "
            "and manage files."
        )
    },

    "venv": {
        "patterns": [
            "what is venv", "virtual environment", "explain virtual environment",
            "python venv"
        ],
        "response": (
            "A virtual environment is an isolated Python environment used to install project-specific packages."
        )
    },

    "pip": {
        "patterns": [
            "what is pip", "pip meaning", "explain pip"
        ],
        "response": (
            "Pip is Python's package installer. It is used to install libraries such as Flask and pytest."
        )
    },

    "pytest": {
        "patterns": [
            "what is pytest", "explain pytest", "pytest meaning"
        ],
        "response": (
            "Pytest is a Python testing framework used to test whether code works correctly."
        )
    },

    "readme": {
        "patterns": [
            "what is readme", "readme file", "explain readme",
            "github readme"
        ],
        "response": (
            "A README file explains the project purpose, features, setup steps, usage instructions, "
            "and technologies used."
        )
    },

    "internship": {
        "patterns": [
            "what is internship", "internship meaning", "explain internship"
        ],
        "response": (
            "An internship is a practical training opportunity where students gain real-world industry experience."
        )
    },

    "software_engineer": {
        "patterns": [
            "what is software engineer", "software engineer meaning",
            "explain software engineer"
        ],
        "response": (
            "A software engineer designs, develops, tests, and maintains software systems."
        )
    },

    "debugging": {
        "patterns": [
            "what is debugging", "debugging meaning", "explain debugging",
            "fix error"
        ],
        "response": (
            "Debugging is the process of finding and fixing errors in a program."
        )
    },

    "error": {
        "patterns": [
            "what is error", "programming error", "explain error",
            "why error happens"
        ],
        "response": (
            "An error is a problem in code that stops the program from working correctly. "
            "Errors can happen due to syntax mistakes, missing files, wrong logic, or missing packages."
        )
    },

    "algorithm": {
        "patterns": [
            "what is algorithm", "algorithm meaning", "explain algorithm"
        ],
        "response": (
            "An algorithm is a step-by-step method used to solve a problem."
        )
    },

    "data": {
        "patterns": [
            "what is data", "data meaning", "explain data"
        ],
        "response": (
            "Data means raw facts, values, or information that can be processed by a computer."
        )
    },

    "database": {
        "patterns": [
            "what is database", "database meaning", "explain database"
        ],
        "response": (
            "A database is an organized collection of data that can be stored, searched, updated, and managed."
        )
    },

    "json": {
        "patterns": [
            "what is json", "json meaning", "explain json"
        ],
        "response": (
            "JSON stands for JavaScript Object Notation. It is a lightweight format used to store "
            "and exchange data."
        )
    },

    "http": {
        "patterns": [
            "what is http", "http meaning", "explain http"
        ],
        "response": (
            "HTTP stands for HyperText Transfer Protocol. It is used for communication between "
            "web browsers and web servers."
        )
    },

    "server": {
        "patterns": [
            "what is server", "server meaning", "explain server"
        ],
        "response": (
            "A server is a computer or program that provides services, data, or resources to other computers."
        )
    },

    "client": {
        "patterns": [
            "what is client", "client meaning", "explain client"
        ],
        "response": (
            "A client is a device or application that requests services or data from a server."
        )
    },

    "localhost": {
        "patterns": [
            "what is localhost", "localhost meaning", "explain localhost",
            "127.0.0.1"
        ],
        "response": (
            "Localhost refers to the local computer. The address 127.0.0.1 is commonly used "
            "to run and test web applications locally."
        )
    },

    "thanks": {
        "patterns": [
            "thanks", "thank you", "thankyou", "thank u", "thanks a lot"
        ],
        "response": "Most welcome! Happy to help."
    },

    "goodbye": {
        "patterns": [
            "goodbye", "see you", "see you later", "talk to you later"
        ],
        "response": "Goodbye! Have a great day."
    }
}


EXIT_COMMANDS = {
    "bye", "exit", "quit", "stop", "close", "end"
}


FALLBACK_RESPONSE = (
    "Sorry, I do not understand that yet. Please ask about AI, Python, Git, GitHub, "
    "Flask, web development, or type 'help' to see what I can do."
)