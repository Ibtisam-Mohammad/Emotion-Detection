FROM python:3.7-slim-buster

ENV PYENV_SHELL=/bin/bash

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y --no-install-recommends build-essential
RUN mkdir -p /app

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

<<<<<<< HEAD
CMD ["uvicorn", "main:app","--port","8080","--host","127.0.0.1","--reload"]
=======
CMD ["uvicorn", "main:app","--reload"]
>>>>>>> 53d5e78f3e61168a9b1f70aa4fbe13c5e070adb5
