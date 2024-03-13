import os

OPENAI_REQUEST_OPTIONS: dict = {
    "max_tokens": 2500,
    "temperature": 0.4,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
