"""
Wrapper around the OpenAI API.
"""


class LLMService:
    """Handles all LLM interactions."""

    def generate(self, prompt: str) -> str:
        raise NotImplementedError