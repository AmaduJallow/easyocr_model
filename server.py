import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware


# import model_easyocr


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
    bytedata = bytes(data.url, "UTF-8")
    print(data.url)
    load_model = pickle.load(open('easyocr.sav', 'rb'))
    value = load_model.readtext(bytedata.decode())
    # data = model_easyocr.image_to_text(data.url)
    string = " "
    for datas in value:
        for line in datas:
            if type(line) == str:
                string += line + ""

    return string
