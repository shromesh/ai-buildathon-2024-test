from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    test,
)  # pwdをappにするならこれでいい。そうでないなら相対パスにする

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test.router)
