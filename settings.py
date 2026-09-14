import os

from dotenv import load_dotenv


load_dotenv()


OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")

if not OLLAMA_API_KEY:
    raise ValueError(
        "OLLAMA_API_KEY is missing. Please add it to your .env file."
    )


OLLAMA_HOST = "https://ollama.com"

MODEL_NAME = "gpt-oss:20b"