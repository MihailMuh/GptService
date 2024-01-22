import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from uvicorn import run

from constants.server_constants import *
from dto.gpt_request import *
from services.gpt_service import GptService


@asynccontextmanager
async def lifespan(app: FastAPI):
    global gpt_service
    gpt_service = GptService()

    yield


logging.basicConfig(format="%(asctime)s %(levelname)s %(funcName)s() --> %(message)s")

gpt_service: GptService
app: FastAPI = FastAPI(default_response_class=ORJSONResponse, lifespan=lifespan)


@app.post("/completion/single")
async def completion(request: GptSingleRequest) -> str:
    return await gpt_service.get_single_response(request.content)


@app.post("/completion/chat")
async def completion(request: GptChatRequest) -> str:
    return await gpt_service.get_chat_response(request.content)


if __name__ == '__main__':
    run("main:app", host=SERVER_HOST, port=SERVER_PORT, workers=SERVER_WORKERS)
