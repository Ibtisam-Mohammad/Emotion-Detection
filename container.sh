#!/bin/bash

cd frontend_react
sh docker-shell.sh
cd ..
cd OpenAI-ASR
sh docker-shell.sh
cd ..
cd preprocessor
sh docker-shell.sh
cd ..
cd Yolov7
sh docker-shell.sh
cd ..
cd sbert
sh docker-shell.sh
cd ..
sudo docker run -d --name nginx -v /conf/nginx/nginx.conf:/etc/nginx/nginx.conf -p 80:80 --network app-network nginx:stable
