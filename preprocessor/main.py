from utils.video import *
from multiprocessing import Pool
from utils.bucket import *
import requests
from pydantic import BaseModel
from utils.audio import *
from google.cloud import storage
import moviepy.editor as mp 
import base64
import glob
import io
from fastapi.responses import FileResponse
from fastapi import FastAPI, Form,  File, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()




origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1",
    "http://localhost:3000",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    filename: str


def make_yolo_call(filename:str):
    url = 'http://127.0.0.1:8989/process'
    json = {
        'filename':filename[:-4]
    }
    x = requests.post(url, json = json)
    if x.status == 200:
        print('Successfully Made YOLO Call')
    else:
        print('Request Unsuccessful:', x.status)




@app.get("/")
async def root():
    return {'message': "Welcome To EDAA"}

@app.post('/video')
async def process_video(data: UploadFile = File()):

    #Hemani is very excited
    array = data.file.read()
    filename = data.filename

    #Write File to memory
    with open(f'{filename}', 'wb') as f:
        f.write(array)
    try:
        #Extract audio and create Chunks
        audio_utils = AudioTools('audio/')
        fileName = audio_utils.extract_audio(filename[:-4], filename)
        audio = audio_utils.read_audio(fileName)
        audio_chunks = audio_utils.create_chunks(audio)
        

        #Create Video Chunks
        pool = Pool(processes=1) 

        result = pool.apply_async(generate_video_chunks, [filename], )

        return {'status':  True}
    except Exception as error:
        print(error)
        return {'status': False}

def callback(event):
    print('Processed Video')


@app.get("/result_names")
async def get_result_names():

    names = []

    thumbnails = list_blobs_with_prefix('thumbnail')

    result = {}

    for fname in thumbnails:
        clean_name = fname.split('/')[-1].replace('.png', '')
        result[clean_name] = {
            'image_name':fname
        }

    return result

@app.post("/get_thumbnail")
async def get_thumbnail(data:Item):

    filename = data.filename

    thumbnails = download_blob_into_memory(filename)
    thumbnails = base64.b64encode(thumbnails)


    return {'image': thumbnails}

def create_dict(data, audio_result, count):
    arr = []
    for interval in data:
        datum = {"interval": interval,
                "sentence": audio_result[interval]["sentence"],
                "prediction": audio_result[interval]["prediction"],
                "people": count[interval]
        }
        arr.append(datum)
    return arr

@app.post("/results")
async def get_results(data:Item):

    filename = data.filename
    ### Get All Available results
    all_results_list  = list_blobs_with_prefix('results')

    for name in all_results_list:
        if name.find('audio')>=0 and name.find(filename)>=0:
            audio_result_name = name
        if name.find('video')>=0 and name.find(filename)>=0:
            video_result_name = name
        
    audio_result = json.loads(download_blob_into_memory(audio_result_name))
    video_result = json.loads(download_blob_into_memory(video_result_name))
    print(video_result)

    ##### CHART 2 ######

    # Creating dictionary that creates seperate dictionaries for each emtion
    #keyed by their interval
    neg = {}
    pos = {}
    neu = {}
    for i in video_result.keys():
        neg[i] = video_result[i]["negative"]
        pos[i] = video_result[i]["positive"]
        neu[i] = video_result[i]["neutral"]


    audio_pos,audio_neg, audio_neu = {}, {}, {}

    for key in audio_result:
        if audio_result[key]['prediction'] == 'positive':
            audio_pos[key] = video_result[key]["positive"]
        elif audio_result[key]['prediction'] == 'negative':
            audio_neg[key] = video_result[key]["negative"]
        else:
            audio_neu[key] = video_result[key]["neutral"]
  


    ### Sort dictionaries
    neg_keys = list(reversed(sorted(neg, key = neg.get)))
    pos_keys = list(reversed(sorted(pos, key = pos.get)))
    neu_keys = list(reversed(sorted(neu, key = neu.get)))


    audio_neg_keys = list(reversed(sorted(audio_neg, key = audio_neg.get)))
    audio_pos_keys = list(reversed(sorted(audio_pos, key = audio_pos.get)))
    audio_neu_keys = list(reversed(sorted(audio_neu, key = audio_neu.get)))


    audio_neg_keys = audio_neg_keys[:5]
    audio_pos_keys = audio_pos_keys[:5]
    audio_neu_keys = audio_neu_keys[:5]





    ### Top 5 ###
    neg_sorted = {i:neg[i] for i in neg_keys[:5]}
    pos_sorted = {i:pos[i] for i in pos_keys[:5]}
    neu_sorted = {i:neu[i] for i in neu_keys[:5]}
    
    ##Chart 2, x, y
    x  = list(neg.keys())
    neg_y = list(neg.values())
    pos_y = list(pos.values())
    neu_y = list(neu.values())

    final_chart2 = []
    for y in [neg_y, pos_y, neu_y]:
        datum = {
            "x": x,
            "y": y
        }
        final_chart2.append(datum)
    #######################################

    ##### TABLE #####
    pos_table  = create_dict(audio_pos_keys, audio_result, audio_pos)
    neg_table = create_dict(audio_neg_keys, audio_result, audio_neg)
    neu_table = create_dict(audio_neu_keys, audio_result, audio_neu)

    final_table = []

    for table, names in zip([pos_table, neg_table, neu_table], ['Positive', 'Negative', 'Neutral']):
        datum = {
            "table": names,
            "rows": table
        }
        final_table.append(datum)

    ################################

    final_chart1 = {}

    for emotion, names in zip([pos, neg, neu], ["Positive", "Negative", "Neutral"]):
        final_chart1[names] = sum(list(emotion.values()))

    final_chart1 = [final_chart1['Positive'], final_chart1['Negative'],final_chart1['Neutral']]

    result = {
        "filename": data.filename,
        "chart1": final_chart1,
        "chart2": final_chart2,
        "table": final_table
    }

    return result







    ### Merge Video And Audio Together

    ### Download Thumbnail as well

    ### Merge THumbnails to filenames 
    

