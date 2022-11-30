FROM python:3.8.2-slim-buster

WORKDIR /code

RUN apt-get update && apt-get -y upgrade

COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./code/requirements.txt


COPY . /code

CMD ["uvicorn", "main:app", "--host", "127.0.0.1","--port","8081","--reload"]
