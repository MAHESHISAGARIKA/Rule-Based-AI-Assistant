"""
CLI runner for Rule Based AI Assistant.

Run:
    python cli.py
"""

from src.rule_based_ai_assistant import RuleBasedAIAssistant


def main():
    assistant = RuleBasedAIAssistant()

    print("=" * 60)
    print("Rule Based AI Assistant")
    print("=" * 60)
    print("Type 'help' to see supported topics.")
    print("Type 'bye', 'exit', or 'quit' to stop.")
    print("-" * 60)

    while True:
        user_message = input("User: ")
        response = assistant.get_response(user_message)
        print(f"Assistant: {response}")

        if assistant.is_exit_command(user_message):
            break


if __name__ == "__main__":
    main()