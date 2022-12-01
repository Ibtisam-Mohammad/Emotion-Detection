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

EXPOSE 8080
CMD ["uvicorn", "main:app","--port","8080","--host","0.0.0.0","--reload"]

