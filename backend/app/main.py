import logging
import os

from fastapi import FastAPI, Request

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {"Hello": "Woraaaaaald"}


# aaa


@app.get("/test")
def read_test():
    return {"Hello": "Test"}


@app.post("/test_post")
async def post_test(request: Request):
    json_body = await request.json()
    logger.info(f"Received JSON body: {json_body}")
    return {"message": "Body logged"}
