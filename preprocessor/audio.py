import moviepy.editor as mp 
import scipy
from math import ceil
import numpy as np

class AudioTools():

    def __init__(self, path=None):
        self.path = path

    
    def extract_audio(self, name='test', videPath = 'test.mp4'):
        name = f"{name}.wav"
        path = self.path + name
        video = self.read_video(videPath)
        video.audio.write_audiofile(path, fps = 16000)
        return path
    
    def read_video(self, path):
        video =  mp.VideoFileClip(path)
        return video

    def read_audio(self, path):
        rate, wav = scipy.io.wavfile.read(path)
        return wav


    def create_chunks(self, audio):
        CHUNK_SIZE = 10
        SAMPLING_RATE = 16000

        chunks = []

        start = 0
        stop = CHUNK_SIZE * SAMPLING_RATE

        chunks_total = ceil(audio.shape[0] / stop)

        # print(chunks_total)

        initial = 1

        while initial <= chunks_total:
            chunk = audio[start:stop, :]
            chunks.append(chunk)
            start = stop 
            initial+=1
            stop+=CHUNK_SIZE * SAMPLING_RATE

        return chunks




