"""
Core assistant logic for the Rule Based AI Assistant.
"""

import re
from difflib import get_close_matches

from .knowledge_base import EXIT_COMMANDS, FALLBACK_RESPONSE, KNOWLEDGE_BASE


class RuleBasedAIAssistant:
    """A professional rule-based AI assistant."""

    def __init__(self):
        self.knowledge_base = KNOWLEDGE_BASE
        self.exit_commands = EXIT_COMMANDS
        self.fallback_response = FALLBACK_RESPONSE
        self.pattern_to_response = self._build_pattern_lookup()

    def _build_pattern_lookup(self):
        """Convert knowledge base patterns into a direct lookup dictionary."""
        lookup = {}

        for intent_data in self.knowledge_base.values():
            response = intent_data["response"]

            for pattern in intent_data["patterns"]:
                normalized_pattern = self.sanitize_input(pattern)
                lookup[normalized_pattern] = response

        return lookup

    @staticmethod
    def sanitize_input(user_input):
        """
        Clean user input.

        Example:
        '  HELLO!!! ' becomes 'hello'
        """
        if not isinstance(user_input, str):
            return ""

        cleaned = user_input.lower().strip()
        cleaned = re.sub(r"[^a-z0-9\s]", "", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned)

        return cleaned

    def is_exit_command(self, user_input):
        """Check whether the user wants to stop the assistant."""
        cleaned_input = self.sanitize_input(user_input)
        return cleaned_input in self.exit_commands

    def get_response(self, user_input):
        """
        Return assistant response based on user input.

        Matching order:
        1. Empty input check
        2. Exit command check
        3. Exact dictionary lookup
        4. Partial keyword matching
        5. Close spelling match
        6. Fallback response
        """
        cleaned_input = self.sanitize_input(user_input)

        if not cleaned_input:
            return "Please type a message."

        if cleaned_input in self.exit_commands:
            return "Goodbye! Have a great day."

        if cleaned_input in self.pattern_to_response:
            return self.pattern_to_response[cleaned_input]

        for pattern, response in self.pattern_to_response.items():
            if pattern in cleaned_input or cleaned_input in pattern:
                return response

        close_matches = get_close_matches(
            cleaned_input,
            self.pattern_to_response.keys(),
            n=1,
            cutoff=0.72,
        )

        if close_matches:
            return self.pattern_to_response[close_matches[0]]

        return self.fallback_response