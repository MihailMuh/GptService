import datetime
import logging

import g4f
from openai import AsyncOpenAI

from constants.gpt_constants import *


class GptService:
    def __init__(self):
        self.__init_logger()
        self.__logger.debug("GptService initialized")
        self.openai_client = AsyncOpenAI(
            api_key=OPENAI_API_KEY,
        )
        self.banned_time = None
        self.is_banned = False

    async def get_single_response(self, message: str) -> str:
        return await self.get_chat_response([{"role": "system", "content": message}])

    async def get_chat_response(self, content: list[dict[str, str]]) -> str:
        self.__logger.debug(f"Questions to ask: {content}")

        if self.is_banned:
            if (datetime.datetime.now() - self.banned_time).total_seconds() >= 600:
                self.is_banned = False
            else:
                response: str = await self.__openai_request(content)
                self.__logger.debug(f"OpenAi Response: {response}")
                return response

        try:
            response: str = await g4f.ChatCompletion.create_async(
                model="gpt-4",
                messages=content,
                provider=g4f.Provider.Bing,
            )

            self.__logger.debug(f"Bing Response: {response}")
            return response

        except Exception as e:
            self.__logger.error(e)
            self.__logger.error("Error in bing. Pausing for 10 minutes...")

            self.banned_time = datetime.datetime.now()
            self.is_banned = True

        return await self.get_chat_response(content)

    async def __openai_request(self, content: list[dict[str, str]]) -> str:
        response = await self.openai_client.chat.completions.create(
            **OPENAI_REQUEST_OPTIONS,
            messages=content
        )

        return response['choices'][0]['message']['content']

    def __init_logger(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG)
