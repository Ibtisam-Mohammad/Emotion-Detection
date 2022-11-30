from fastapi import FastAPI, Form,  File, UploadFile, Body
from typing import Any, Dict, AnyStr, List, Union
import numpy as np
from pydantic import BaseModel
import json

class Item(BaseModel):
    sentences: List[str]
    filename: str
    
app = FastAPI()


@app.get("/")
async def root():
    return {'message': "This is Sentence Bert In the House"}

@app.post('/predict')
async def predict(data: Item = None):
    sentences = data.sentences
    filename = data.filename
    print([sentences,filename])
    return [sentences,filename]