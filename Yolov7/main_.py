from typing import Optional, Union
from fastapi import FastAPI, Request, File,UploadFile
# import numpy as np
import requests
from pydantic import BaseModel
import pickle
import io
import json
import os
import subprocess
import datetime
import base64

app = FastAPI()

    
@app.post('/predict_video')
async def predict(file: Optional[bytes] = File(default=None)):
    #print(type(file))
    #decode = base64.standard_b64decode(file[22:])
    #with open('test.mp4', 'wb') as f:
    #    f.write(decode)
    os.system('entry_video.bat')
    with open('result.pickle','rb') as f:
        output = pickle.load(f)
    return output


