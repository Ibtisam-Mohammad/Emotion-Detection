try:
    from utils.text import *
    from utils.bucket import *

except:
    from .utils.text import *
    from .utils.bucket import *


from fastapi import FastAPI, Form,  File, UploadFile, Body
from typing import Any, Dict, AnyStr, List, Union
import numpy as np
from pydantic import BaseModel

import json


bucket_name = 'edaa_bucket'

class Item(BaseModel):
    sentences: List[str]
    filename: str


app = FastAPI()

model = import_model()

@app.get("/")
async def root():
    return {'message': "This is Sentence Bert In the House"}

@app.post('/predict')
async def predict(data: Item = None):
    sentences = data.sentences
    dataset = encode_examples(sentences).batch(1)
    predictions = model.predict(dataset)
    mapping = {0:'negative', 1:'neutral', 2:'positive'}
    print(predictions)
    decoded_predictions = [mapping[np.argmax(p)] for p in predictions]
    upload = {}
    start = 0
    stop = 10

    for i in range(len(decoded_predictions)):
        key = f'{start}_{stop}'
        upload[key] = {
            'sentence': sentences[i],
            'prediction': decoded_predictions[i],
            'start':start,
            'stop': stop
        }
        start = stop
        stop+=10

    print(upload)
    json_file = json.dumps(upload, indent=2).encode('utf-8')

    try:
        upload_blob_from_memory(bucket_name, 
        contents= json_file,
        destination_blob_name=f'results/audio_{data.filename}.json')
    except Exception as e:
        print(e)

    

    return {'results': 'Processed'}

@app.get("/results")
async def get_results():
    pass

