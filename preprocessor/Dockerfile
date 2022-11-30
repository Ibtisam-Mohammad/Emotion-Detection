FROM python:3.8.2-slim-buster

WORKDIR /code

RUN apt-get update && apt-get -y upgrade && apt install -y wget

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

RUN wget https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/ffmpeg.linux64
RUN mkdir ~/.imageio
RUN mkdir ~/.imageio/ffmpeg/
RUN mv ffmpeg.linux64 ~/.imageio/ffmpeg/ffmpeg-linux64-v3.3.1

COPY . ./app

EXPOSE 8002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port" ,"8002", "--reload"]
