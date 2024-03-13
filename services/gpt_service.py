import logging

from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

from constants.gpt_constants import *


class GptService:
    def __init__(self):
        self.__init_logger()
        self.__logger.debug("GptService initialized")
        self.openai_client = AsyncOpenAI(
            api_key=OPENAI_API_KEY,
        )

    async def get_single_response(self, message: str, model: str) -> str:
        return await self.get_chat_response([{"role": "system", "content": message}], model)

    async def get_chat_response(self, content: list[dict[str, str]], model: str) -> str:
        self.__logger.debug(f"Questions to ask: {content}")

        response: ChatCompletion = await self.openai_client.chat.completions.create(
            **OPENAI_REQUEST_OPTIONS | {"model": model},
            messages=content
        )
        response_str: str = response.choices[0].message.content

        self.__logger.debug(f"OpenAi Response: {response_str}")
        return response_str

    def __init_logger(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG)
