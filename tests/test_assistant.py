from src.rule_based_ai_assistant import RuleBasedAIAssistant


def test_greeting_response():
    assistant = RuleBasedAIAssistant()
    response = assistant.get_response("hello")
    assert "Hello" in response


def test_input_sanitization():
    assistant = RuleBasedAIAssistant()
    response1 = assistant.get_response("HELLO!!!")
    response2 = assistant.get_response("hello")
    assert response1 == response2


def test_ai_definition_response():
    assistant = RuleBasedAIAssistant()
    response = assistant.get_response("what is ai")
    assert "Artificial Intelligence" in response


def test_fallback_response():
    assistant = RuleBasedAIAssistant()
    response = assistant.get_response("some unknown question")
    assert "Sorry" in response


def test_exit_command():
    assistant = RuleBasedAIAssistant()
    assert assistant.is_exit_command("bye") is True
    assert assistant.get_response("bye") == "Goodbye! Have a great day."