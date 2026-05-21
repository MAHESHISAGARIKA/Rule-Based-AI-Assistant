"""
Web interface for Rule Based AI Assistant.

Run:
    python web_app.py

Then open:
    http://127.0.0.1:5000
"""

from flask import Flask, jsonify, render_template, request

from src.rule_based_ai_assistant import RuleBasedAIAssistant

app = Flask(__name__)
assistant = RuleBasedAIAssistant()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")
    response = assistant.get_response(user_message)

    return jsonify(
        {
            "reply": response,
            "is_exit": assistant.is_exit_command(user_message),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)