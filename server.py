from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

import model_easyocr


class imageUrl(BaseModel):
    url: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
async def get():
    return {"Hello world"}


@app.post('/url')
async def imager(data: imageUrl):
    print(data.url)
    data = model_easyocr.image_to_text(data.url)
    return data
