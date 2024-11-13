import logging
import os
from fastapi import APIRouter, Depends, HTTPException, Response, status, Security
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(tags=["test"])


@router.get("/")
def read_root():
    return {"Hello": "Wor"}


@router.get("/test")
def read_test():
    return {"Hello": "Test"}


class testRequestBody(BaseModel):
    query: str


@router.post("/test_post")
async def post_test(body: testRequestBody):
    logger.info(f"Received JSON body: {body.query}")
    return {"message": f"{body.query} logged"}
