from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def chat(self, messages: list[dict]) -> str:
        """
        Send messages to the LLM and return the response text.
        """
        pass