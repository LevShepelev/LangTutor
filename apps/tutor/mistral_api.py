"""
Wrapper for interacting with the Mistral API.
"""

# pylint: disable=import-error,too-few-public-methods
import time

from mistralai import Mistral


class MistralAPI:
    """API wrapper for Mistral via mistralai."""

    def __init__(self, api_key: str, rate_limit: float = 1.0) -> None:
        self.llm_model = Mistral(api_key=api_key)
        self.rate_limit = rate_limit
        self.last_request_time = 0

    def _apply_rate_limit(self) -> None:
        """Apply rate limiting to API calls."""
        elapsed = time.time() - self.last_request_time
        min_interval = 1 / self.rate_limit
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

    def chat_complete(
        self,
        messages: list,
        model: str = "mistral-large-latest",
        temperature: float = 0.2,
    ) -> str:
        """
        Complete a chat with the given messages.

        Args:
            messages (list): List of dicts with keys "role" and "content".
            model (str): The model identifier.
            temperature (float): Response determinism parameter.

        Returns:
            str: The response from the API.
        """
        self._apply_rate_limit()
        chat_response = self.llm_model.chat.complete(
            model=model, messages=messages, temperature=temperature
        )
        self.last_request_time = time.time()
        answer = chat_response.choices[0].message.content
        return answer
