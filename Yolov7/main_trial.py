from typing import Optional, Union, List
from fastapi import FastAPI, Request, File,UploadFile
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    filename: str

@app.post('/')
async def predict(data: Item = None):
    print(data.filename)
    return data.filename