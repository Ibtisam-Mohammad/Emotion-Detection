import os
import shutil
import cv2
import pickle
import os
import json
from frame import save_frame
from typing import Optional, Union, List
from fastapi import FastAPI, Request, File,UploadFile
from pydantic import BaseModel
from glob import glob
from detect_trial import detect
from bucket import download_blob, list_blobs, upload_blob,upload_blob_from_memory

app = FastAPI()

class Item(BaseModel):
    filename: str

@app.post('/')
async def predict(data: Item = None):

    print(data.filename)
    return data.filename
    # dir_={}
    # list_of_files = list_blobs()
    # print(list_of_files)
    # file_name = data.filename
    # for fname in list_of_files:
    #     if file_name.find(fname)>=0:
    #         print(fname)
    #         fname=fname[7:]
    #         download_blob('edaa_bucket','chunks/'+fname, 'video_data/input_dir/'+fname)

    # video_paths = glob("video_data/input_dir/*")
    # for path in video_paths:
    #     save_frame(path, "video_data/output_frames", gap=25)
    #     folder_name=path.split('\\')[-1].split('.')[0]
    #     detect(weights='weights/face.pt',source='video_data/output_frames/input_dir/'+folder_name,img_size=640,conf_thres=0.90,device='0',view_img=False,\
    #         save_txt=False,save_conf=False,save_crop=True,\
    #             project='video_data/output_faces', name=folder_name,\
    #             no_trace=True, classes = [0])

    #     detect(weights='weights/emotions.pt',source='video_data/output_faces/'+folder_name+'/crops/face',img_size=640,conf_thres=0.20,device='0',view_img=False,\
    #         save_txt=False,save_conf=False,save_crop=True,\
    #             project='video_data/output_emotions', name=folder_name,\
    #             no_trace=True, classes = [0,1,2,3,4,5,6,7,8])

    #     dict_e={}
    #     for i in os.listdir('video_data/output_emotions/'+folder_name+'/crops'):
    #         dict_e[i]=len(os.listdir('video_data/output_emotions/'+folder_name+'/crops/'+i))

    #     negative,neutral,positive=0,0,0
    #     for i in dict_e.keys():
    #         if i in ['anger','contempt','disgust','fear','sad']:
    #             negative = negative + dict_e[i]
    #         elif i == 'neutral':
    #             neutral = dict_e['neutral']
    #         elif i in ['happy','surprise']:
    #             positive = positive + dict_e[i]
    #     output = {
    #             'positive':positive,
    #             'neutral':neutral,
    #             'negative':negative
    #             }
    #     upload_name =  '_'.join(folder_name.split('_')[-2:])
    #     dir_[upload_name]=output
    # dir_ = json.dumps(dir_, indent=2).encode('utf-8')
    # upload_blob_from_memory('edaa_bucket', dir_, f'results/video_{file_name}.json')

# shutil.rmtree('video_data/output_frames/')
# os.mkdir('video_data/output_frames/')
# shutil.rmtree('video_data/output_faces/')
# os.mkdir('video_data/output_faces/')
# shutil.rmtree('video_data/output_emotions/')
# os.mkdir('video_data/output_emotions/')
# shutil.rmtree('video_data/input_dir/')
# os.mkdir('video_data/input_dir/')