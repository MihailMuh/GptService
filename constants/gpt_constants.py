import os

OPENAI_GPT_MODEL: str = "gpt-4-1106-preview"

OPENAI_REQUEST_OPTIONS: dict = {
    "model": OPENAI_GPT_MODEL,
    "max_tokens": 2500,
    "temperature": 0.4,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
