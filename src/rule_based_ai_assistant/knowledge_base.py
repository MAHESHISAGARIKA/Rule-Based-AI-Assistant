"""
Knowledge base for the Rule Based AI Assistant.

Each intent contains:
- patterns: possible user inputs
- response: chatbot reply
"""

KNOWLEDGE_BASE = {
    "greeting": {
        "patterns": [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        ],
        "response": "Hello! I am Rule Based AI Assistant. How can I help today?",
    },

    "creator": {
        "patterns": [
            "who created you",
            "who made you",
            "who developed you",
            "your developer",
        ],
        "response": "I was developed as an internship project to demonstrate rule-based AI logic.",
    },

    "ai_definition": {
        "patterns": [
            "what is ai",
            "what is artificial intelligence",
            "explain ai",
            "define ai",
        ],
        "response": (
            "Artificial Intelligence is the ability of a computer system to simulate "
            "human-like tasks such as answering questions, reasoning, and decision-making."
        ),
    },

    "rule_based_ai": {
        "patterns": [
            "what is rule based ai",
            "what is rule based chatbot",
            "explain rule based chatbot",
            "how rule based chatbot works",
        ],
        "response": (
            "A rule-based chatbot works using predefined rules. It checks the user input "
            "and selects a response based on matching patterns."
        ),
    },

    "python": {
        "patterns": [
            "what is python",
            "explain python",
            "python",
        ],
        "response": (
            "Python is a beginner-friendly programming language used for web development, "
            "data analysis, automation, AI, and machine learning."
        ),
    },

    "git": {
        "patterns": [
            "what is git",
            "explain git",
            "git",
        ],
        "response": (
            "Git is a version control system. It helps developers track code changes "
            "and manage project history."
        ),
    },

    "github": {
        "patterns": [
            "what is github",
            "explain github",
            "github",
        ],
        "response": (
            "GitHub is an online platform for storing, sharing, and managing code projects "
            "using Git."
        ),
    },

    "vs_code": {
        "patterns": [
            "what is vs code",
            "what is visual studio code",
            "explain vs code",
            "vs code",
        ],
        "response": (
            "VS Code is a popular code editor used by developers to write, run, and manage code."
        ),
    },

    "internship_project": {
        "patterns": [
            "what is this project",
            "explain this project",
            "project idea",
            "about this project",
        ],
        "response": (
            "This project is a Rule Based AI Assistant. It uses input cleaning, pattern matching, "
            "a knowledge base, fallback responses, and exit commands."
        ),
    },

    "help": {
        "patterns": [
            "help",
            "commands",
            "what can you do",
            "features",
        ],
        "response": (
            "I can answer simple questions about AI, Python, Git, GitHub, VS Code, "
            "and this internship project. Try asking: 'what is ai' or 'what is github'."
        ),
    },

    "thanks": {
        "patterns": [
            "thanks",
            "thank you",
            "thankyou",
        ],
        "response": "Most welcome! Happy to help.",
    },
}

EXIT_COMMANDS = {"bye", "exit", "quit", "stop"}

FALLBACK_RESPONSE = (
    "Sorry, I do not understand that yet. Please try asking about AI, Python, Git, GitHub, or type 'help'."
)