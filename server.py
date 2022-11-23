from fastapi import FastAPI
from pydantic import BaseModel
import model_easyocr


class imageUrl(BaseModel):
    url: str


app = FastAPI()


@app.get('/')
async def get():
    return {"Hello world"}


@app.post('/url')
async def imager(data: imageUrl):
    print(data.url)
    data = model_easyocr.image_to_text(data.url)
    return data
