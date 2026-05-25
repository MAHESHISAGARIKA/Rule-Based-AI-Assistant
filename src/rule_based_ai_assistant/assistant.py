"""
Core assistant logic for Rule Based AI Assistant.
"""

import re
from difflib import get_close_matches

from .knowledge_base import EXIT_COMMANDS, FALLBACK_RESPONSE, KNOWLEDGE_BASE


class RuleBasedAIAssistant:
    """
    Professional rule-based chatbot.

    Matching methods:
    1. Clean user input
    2. Check exit command
    3. Exact pattern matching
    4. Partial pattern matching
    5. Fuzzy spelling correction
    6. Fallback response
    """

    def __init__(self):
        self.knowledge_base = KNOWLEDGE_BASE
        self.exit_commands = EXIT_COMMANDS
        self.fallback_response = FALLBACK_RESPONSE
        self.pattern_to_response = self._build_pattern_lookup()

    def _build_pattern_lookup(self):
        """
        Build a dictionary:
        pattern -> response
        """
        lookup = {}

        for intent_data in self.knowledge_base.values():
            response = intent_data["response"]

            for pattern in intent_data["patterns"]:
                cleaned_pattern = self.sanitize_input(pattern)
                lookup[cleaned_pattern] = response

        return lookup

    @staticmethod
    def sanitize_input(user_input):
        """
        Clean user input.

        Example:
        '  WHAT is AI??? ' -> 'what is ai'
        """
        if not isinstance(user_input, str):
            return ""

        cleaned = user_input.lower().strip()
        cleaned = re.sub(r"[^a-z0-9\s.]", "", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned)

        return cleaned

    def is_exit_command(self, user_input):
        """
        Check whether the input is an exit command.
        """
        cleaned_input = self.sanitize_input(user_input)
        return cleaned_input in self.exit_commands

    def get_response(self, user_input):
        """
        Generate chatbot response.
        """
        cleaned_input = self.sanitize_input(user_input)

        if not cleaned_input:
            return "Please type a message."

        if self.is_exit_command(cleaned_input):
            return "Goodbye! Have a great day."

        # 1. Exact match
        if cleaned_input in self.pattern_to_response:
            return self.pattern_to_response[cleaned_input]

        # 2. Partial match
        for pattern, response in self.pattern_to_response.items():
            if pattern in cleaned_input or cleaned_input in pattern:
                return response

        # 3. Fuzzy match for small spelling mistakes
        close_matches = get_close_matches(
            cleaned_input,
            self.pattern_to_response.keys(),
            n=1,
            cutoff=0.72
        )

        if close_matches:
            best_match = close_matches[0]
            return self.pattern_to_response[best_match]

        # 4. Fallback response
        return self.fallback_response