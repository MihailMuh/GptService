from pydantic import BaseModel


class GptSingleRequest(BaseModel):
    content: str
    model: str


class GptChatRequest(BaseModel):
    content: list[dict[str, str]]
    model: str
