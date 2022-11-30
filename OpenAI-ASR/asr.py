import os
import warnings
import numpy as np
import torchaudio 
import torch
import pickle
from utils import load_model, pad_or_trim, log_mel_spectrogram
from utils import DecodingOptions
from tqdm import tqdm
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


def main(files, model='base.en', language='en'):
    """
    Main function
    :param file: File to be processed
    :param model: Model to be loaded
    :param language: Language to be used
    :return:
    """
    #Loading the model
    model, options = loadModel(model, language)
    #Pre-processing of the audio file
    texts = []
    for file in files:
        mels = preprocess(file)
        text = model.decode(mels, options)
        texts.append(text.text)
    return texts

for file_name in os.listdir('audios/'):
    print('Creating file:',file_name)
    result = main(['audios/'+file_name])
    with open('output/'+file_name.split('.')[0]+'.txt','w+') as r:
        r.write(result[0][:len(result[0])//2])
        print('file generated..........')