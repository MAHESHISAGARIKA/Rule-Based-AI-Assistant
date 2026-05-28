# Rule Based AI Assistant

Rule Based AI Assistant is a beginner-friendly artificial intelligence chatbot project developed as part of an internship foundation task. This assistant responds to user messages using predefined rules instead of machine learning or deep learning models.

The main purpose of this project is to understand the foundation of AI logic through control flow, decision-making, input sanitization, pattern matching, fallback responses, and continuous user interaction.

---

## Project Overview

This project demonstrates how a simple AI assistant can be built using rule-based logic. The assistant takes user input, cleans the input, checks it against a predefined knowledge base, and returns a suitable response.

If the assistant does not understand the user input, it provides a fallback response. The project also supports exit commands such as `bye`, `exit`, `quit`, and `stop`.

---

## Features

- Rule-based chatbot response system
- Predefined knowledge base
- Input sanitization
- Greeting command handling
- Exit command handling
- Fallback response for unknown inputs
- Dictionary-based pattern matching
- Fuzzy matching for small spelling mistakes
- Command-line interface
- Professional web interface
- Flask backend server
- Unit testing using pytest
- Clean and organized project structure

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Pytest
- Git
- GitHub
- VS Code

---

## Project Structure

```text
Rule-Based-AI-Assistant/
│
├── src/
│   └── rule_based_ai_assistant/
│       ├── __init__.py
│       ├── assistant.py
│       └── knowledge_base.py
│
├── static/
│   └── styles.css
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_assistant.py
│
├── cli.py
├── web_app.py
├── requirements.txt
└── README.md