from fastapi.encoders import jsonable_encoder
from typing import Optional
from fastapi import FastAPI
import config

app = FastAPI()


@app.get('/')
def hello():
    return {'Hello': 'World'}


@app.get('/cv/')
def cv():
    myCVJson = jsonable_encoder(config.myCV)
    return myCVJson



