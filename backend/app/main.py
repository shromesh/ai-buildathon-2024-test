import logging
import os

from fastapi import FastAPI, Request

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def read_test():
    return {"Hello": "Test"}


@app.post("/test_post")
async def post_test(request: Request):
    json_body = await request.json()
    logger.info(f"Received JSON body: {json_body}")
    return {"message": "Body logged"}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
