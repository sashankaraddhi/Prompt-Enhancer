from ollama import Client

from settings import OLLAMA_API_KEY, OLLAMA_HOST, MODEL_NAME
from base import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(self, model: str = MODEL_NAME):
        self.model = model

        self.client = Client(
            host=OLLAMA_HOST,
            headers={
                "Authorization": f"Bearer {OLLAMA_API_KEY}"
            }
        )

    def chat(self, messages: list[dict]) -> str:
        """
        Send conversation messages to Ollama
        and return the model's response text.
        """

        response = self.client.chat(
            model=self.model,
            messages=messages,
            format="json"
        )

        return response["message"]["content"]