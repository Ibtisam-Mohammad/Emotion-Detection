from typing import Optional, Union, List
from fastapi import FastAPI, Request, File,UploadFile
import requests
import numpy as np
from pydantic import BaseModel
import pickle
import io
import json
import os
import datetime
import base64
import warnings
# import torchaudio 
import torch
from utils import load_model, pad_or_trim, log_mel_spectrogram
from utils import DecodingOptions
from tqdm import tqdm
app = FastAPI()

#Checking available ceces 
DEVICE = "cpu" # if torch.cuda.is_available() else "cpu"

def preprocess(file, device=DEVICE):
    """
    Pre-processing of the audio file
    :param file: File to be processed
    :param device: Device to be used
    :return:
    """
    #Loading the audio file
    audio = torch.from_numpy(file)
    # audio, samplingRate = torchaudio.load(file)
    # audio = audio

    #Pre-processing of the audio file
    audio = pad_or_trim(audio.flatten()).to(DEVICE)
    mel = log_mel_spectrogram(audio)
    return mel


def loadModel(model, language='en'):
    """
    Load the model
    :param model: Model to be loaded
    :return:
    """
    print(f'Loading f{model} model...')
    model = load_model(model).to(DEVICE)

    print('Initializing DecodingOptions...')
    options = DecodingOptions(language= language, without_timestamps=False,fp16 = False)
    return model, options



class Item(BaseModel):
    chunks: list
    filename: str
print('load model')
model, options = loadModel('base.en')

#From preprocessor to ASR
@app.post('/predict')
async def predict(data: Item = None):
    chunks = data.chunks
    filename = data.filename
    texts=[]
    for chunk in chunks:
        chunk = np.array(chunk,dtype='float32')
        mel = preprocess(chunk)
        text = model.decode(mel, options)
        text=text.text
        text = text[:len(text)//2]
        texts.append(text)
    upload ={
        "sentences":texts,
        "filename":filename
    }
    print('.........................................',upload)
    make_asr_call(upload)
    return {'stat':'forwarded to bert'}

# TO ADD BERT API CALL
def make_asr_call(obj):
    url = 'http://try:8081/predict'
    x = requests.post(url, json = obj)
    if x.status_code == 200:
        print('Successfully Made Bert Call')
    else:
        print('Request Unsuccessful:', x.status_code)


