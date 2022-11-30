import cv2 as cv2
import datetime
import numpy as np
import os 
from app.bucket import upload_blob, upload_blob_from_memory

bucket_name = 'edaa_bucket'

def clip_video(filename,origintime,starttime,endtime,outputfilename):
    
    cap = cv2.VideoCapture(filename) #Read Frame
    fps=cap.get(cv2.CAP_PROP_FPS)

    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #height
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #width

    startframe=fps*(starttime-origintime).total_seconds()  #get the start frame
    endframe=fps*(endtime-origintime).total_seconds()  #get the end frame

    #video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    out1 = cv2.VideoWriter(outputfilename,fourcc, fps, (width,height))

    counter = 1 #set counter
    while(cap.isOpened()):           #while the cap is open

        ret, frame = cap.read()       #read frame
        if frame is None:             #if frame is None
            break  

        frame=cv2.resize(frame, (width,height))  #resize the frame
        if counter>=startframe and counter<=endframe:  #check for range of output
            out1.write(frame)  #output 

        key = cv2.waitKey(1) & 0xFF

        counter+=1  #increase counter

    #release the output and cap  
    out1.release()
    cv2.destroyAllWindows()



def divide_in_videos(filename):

    cap = cv2.VideoCapture(filename) #Read Frame
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps=cap.get(cv2.CAP_PROP_FPS)    #Extract the frame per second (fps)
    seconds = round(frames / fps)
    video_time = datetime.timedelta(seconds=seconds)

    print(f"duration in seconds: {seconds}")
    print(f"video time: {video_time}")

    video_time = datetime.datetime.strptime(str(video_time),"%H:%M:%S")
    
    origin="00:00:00"          #the origin
    start="00:00:00"           #specify start time in hh:mm:ss
    end = "00:00:10"           #specify end time in hh:mm:ss

    origintime=datetime.datetime.strptime(origin,"%H:%M:%S") #origin 
    starttime=datetime.datetime.strptime(start,"%H:%M:%S")  #start time
    endtime=datetime.datetime.strptime(end,"%H:%M:%S")      #end time
    
    starttimes = []
    endtimes = []

    while endtime < video_time:
        starttimes.append(starttime)
        endtimes.append(endtime)
        
        print(starttime,endtime)
        
        time_change = datetime.timedelta(seconds=10)
        starttime = endtime
        endtime = endtime + time_change
        
    starttimes.append(starttime)
    endtimes.append(endtime) 
    print("last : ",starttime,endtime) 
    
    return starttimes,endtimes


def read_cv2_video(path):

  #Read Video from Path
  video = cv2.VideoCapture(path)

  #Extract number of frames and frames per second 
  fps = video.get(cv2.CAP_PROP_FPS)
  print('frames per second =',fps)
  frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
  print('duration of the video is around', frames//fps, "seconds")

  success = 1
  count = 0 
  images = []
  while success:

    success, frame = video.read()
    images.append(frame)
    count+=1
  print(count, 'frames extracted from the video')
  return images


def generate_video_chunks(filename):

    cap = cv2.VideoCapture(filename) #Read Frame
    while(cap.isOpened()):           #while the cap is open
        ret, frame = cap.read()       #read frame
        break
    title = "thumbnail/" + filename[:-4] + ".png"
    upload_blob(bucket_name, 
            source_file_name= title,
            destination_blob_name=title)

    cv2.imwrite(title,frame)

    origin="00:00:00"  
    starttimes, endtimes = divide_in_videos(filename)
    count = 0
    folder = filename[:-4]
    for starttime,endtime in zip(starttimes,endtimes):
        origintime=datetime.datetime.strptime(origin,"%H:%M:%S")
        clip_video(filename,origintime,starttime,endtime,f'chunks/{filename[:-4]}_{count}_{count+10}.mp4')
        _filename = f'chunks/{filename[:-4]}_{count}_{count+10}.mp4'
        try:
            upload_blob(bucket_name, 
            source_file_name= _filename,
            destination_blob_name=_filename)
        except Exception as e:
            print(e)
        count +=10
