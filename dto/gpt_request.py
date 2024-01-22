from pydantic import BaseModel


class GptSingleRequest(BaseModel):
    content: str


class GptChatRequest(BaseModel):
    content: list[dict[str, str]]
