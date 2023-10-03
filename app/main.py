import openai

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routers import file

app = FastAPI()
app.include_router(file.router)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = ""
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                               messages=[{"role": "user", "content": "Hello world"}])
