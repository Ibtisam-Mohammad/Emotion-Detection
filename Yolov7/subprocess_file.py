import shutil
import matplotlib.pyplot as plt
import cv2
import subprocess
import pickle
import os
import json
from frame import save_frame
from typing import Optional, Union, List
from fastapi import FastAPI, Request, File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from glob import glob
from detect_trial import detect
from bucket import download_blob, list_blobs, upload_blob,upload_blob_from_memory

app = FastAPI()


class Item(BaseModel):
    filename: str

@app.post('/predict_video')
async def predict(data: Item = None):
    dir_={}
    list_of_files = list_blobs()
    length_ = len(list_of_files)
    print(list_of_files) ###['chunks/talking_dog_0_10.mp4', 'chunks/talking_dog_10_20.mp4',....]
    file_name = data.filename
    print(file_name)#### 'talking_dog'
    for fname in list_of_files:
        if fname.find(file_name)>=0:
            print(fname)
            fname=fname[7:]
            download_blob('edaa_bucket','chunks/'+fname, 'video_data/input_dir/'+fname)

    video_paths = glob("video_data/input_dir/*")
    for path in video_paths:
        save_frame(path, "video_data/output_frames", gap=25)
        folder_name=path.split('/')[-1].split('.')[0]   # use ('\\') on Windows
        print('PATH:',path,'\n',folder_name)
        detect(weights='weights/face.pt',source='video_data/output_frames/'+folder_name,img_size=640,conf_thres=0.70,device='cpu',view_img=False,\
            save_txt=False,save_conf=False,save_crop=True,\
                project='video_data/output_faces', name=folder_name,\
                no_trace=True, classes = [0])

        detect(weights='weights/emotions.pt',source='video_data/output_faces/'+folder_name+'/crops/face',img_size=640,conf_thres=0.20,device='cpu',view_img=False,\
            save_txt=False,save_conf=False,save_crop=True,\
                project='video_data/output_emotions', name=folder_name,\
                no_trace=True, classes = [0,1,2,3,4,5,6,7,8])

        dict_e={}
        for i in os.listdir('video_data/output_emotions/'+folder_name+'/crops'):
            dict_e[i]=len(os.listdir('video_data/output_emotions/'+folder_name+'/crops/'+i))

        negative,neutral,positive=0,0,0
        for i in dict_e.keys():
            if i in ['anger','contempt','disgust','fear','sad']:
                negative = negative + dict_e[i]
            elif i == 'neutral':
                neutral = dict_e['neutral']
            elif i in ['happy','surprise']:
                positive = positive + dict_e[i]
        output = {
                'positive':positive,
                'neutral':neutral,
                'negative':negative//10
                }
        upload_name =  '_'.join(folder_name.split('_')[-2:])
        dir_[upload_name]=output
    dir_ = json.dumps(dir_, indent=2).encode('utf-8')
    upload_blob_from_memory('edaa_bucket', dir_, f'results/video_{file_name}.json')

    try:
        shutil.rmtree('video_data/output_frames/')
    except:
        print("No output_frames")
    os.mkdir('video_data/output_frames/')

    try:
        shutil.rmtree('video_data/output_faces/')
    except:
        print("No output_faces")
    os.mkdir('video_data/output_faces/')

    try:
        shutil.rmtree('video_data/output_emotions/')
    except:
        print("No output_emotions")
    os.mkdir('video_data/output_emotions/')

    try:
        shutil.rmtree('video_data/input_dir/')
    except:
        print("No input_dir")
    os.mkdir('video_data/input_dir/')

    print("Check your bucket for results")

