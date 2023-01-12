# EDAA

Hello everyone,

This repository contains the EDAA app. EDAA stands for Emotion Detection and Analysis. It is a web application which will create a report of audience reactions. We take into consideration, video (facial expressions of the audience) and text (context of the speech) data. This app will help public speakers improve their speech. Please read more about our app in the about section of our web app. 

[Link](https://youtu.be/G5-u3YE2TSQ?t=933) to the presentation on youtube

The following is a diagram of the architecture of our web app:
![img](https://github.com/aamir09/FinalSubmissionAI5/blob/main/webapp_architecture.PNG "webapp_architecture.PNG")

As you can see from the plot above,
The user will input a video into the web app. The [Upload](https://github.com/aamir09/FinalSubmissionAI5/blob/main/frontend_react/src/components/Upload.js) component of the frontend-react downloads the video to the server after encoding it.
This video is then taken by the [preprocessor](https://github.com/aamir09/FinalSubmissionAI5/tree/main/preprocessor) which first decodes it. 
Once decoded audio is extracted from the video using moviepy.
Then it is divided into chunks by using the preprocessor. The preprocessor divides the audio into 10 second chunks.
These audio chunks are the converted to text using the [ASR container](https://github.com/aamir09/FinalSubmissionAI5/tree/main/OpenAI-ASR).
These sentences are analysed using [SBert](https://github.com/aamir09/FinalSubmissionAI5/tree/main/sbert).
The sbert container predicts the sentiment of the model and saves the audio predictions to the GCS bucket.
Here is a screenshot of the bucket to get a basic idea of the structure.
![img](https://github.com/aamir09/FinalSubmissionAI5/blob/main/GCS_bucket.jpeg)
The results look something like this :</br>
{ <br/>
  "0_10": { <br/>
    "sentence": "I'm goin", <br/>
    "prediction": "negative", <br/>
    "start": 0, <br/>
    "stop": 10 <br/>
  }, <br/>
  "10_20": { <br/>
    "sentence": "to go to the museum", <br/>
    "prediction": "neutral", <br/>
    "start": 10, <br/>
    "stop": 20 <br/>
  }, <br/>
  "20_30": { <br/>
    "sentence": "Good Bye", <br/>
    "prediction": "neutral", <br/>
    "start": 20, <br/>
    "stop": 30<br/>
  } <br/>
} <br/>
The key of the dictionary specify the start and the stop time, i.e. the interval. the value is a dictionay which has the the following information :
- sentence - this has been predicted by the asr model when the input audio chunk is given as input.
- prediction - this has been predicted by the sentence bert model when the sentence is given as input.
- start - start time
- stop - stop time

Similarly the video chunks are created by the preprocessor and uploaded to GCS bucket. The yolo container takes these chunks as input to the [yolo container](https://github.com/aamir09/FinalSubmissionAI5/tree/main/Yolov7).
The results look something like this :</br>
{</br>
  "50_60": {</br>
    "positive": 2,</br>
    "neutral": 0,</br>
    "negative": 39</br>
  },</br>
  "20_30": {</br>
    "positive": 1,</br>
    "neutral": 2,</br>
    "negative": 45</br>
  },</br>
  "10_20": {</br>
    "positive": 1,</br>
    "neutral": 0,</br>
    "negative": 35</br>
  }</br>
  
 The above results are taken back to the frontend and we use plotly.js to make plots.
 
# Deployment instructions

- Pull the above repository to your local machine
- change the directory to frontend_react and run the docker-shell.sh file.
~~~
cd frontend_react
sh docker-shell.sh
~~~
- Create a conf nginx folder
~~~
mkdir nginx
~~~
- we will add the file nginx.conf in which we will the following contents
~~~
user  nginx;
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;
events {
    worker_connections  1024;
}
http {
	client_max_body_size 50M;
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    tcp_nopush     on;
    keepalive_timeout  65;
	types_hash_max_size 2048;
	server_tokens off;
    gzip  on;
	gzip_disable "msie6";

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

	server {
		listen 80;

		server_name localhost;

		# Nginx default
		# location / {
		# 	root   /usr/share/nginx/html;
		# 	index  index.html index.htm;
		# }

		error_page   500 502 503 504  /50x.html;
		location = /50x.html {
			root   /usr/share/nginx/html;
		}
		# API
		location /api {
			rewrite ^/api/(.*)$ /$1 break;
			proxy_pass http://preprocessor:8005;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header Host $http_host;
			proxy_redirect off;
			proxy_buffering off;
		}

		# Frontend
		location / {
			rewrite ^/(.*)$ /$1 break;
			proxy_pass http://frontend:3000;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header Host $http_host;
			proxy_redirect off;
			proxy_buffering off;
		}
	}

	#include /etc/nginx/sites-enabled/*;
}

~~~
- Run the following command
~~~
sudo docker run -d --name nginx -v /conf/nginx/nginx.conf:/etc/nginx/nginx.conf -p 80:80 --network app-network nginx:stable
~~~
- create the following folders inside the Yolov7 folder. We couldn't add this here as github does not save empty folders.
~~~
mkdir Yolov7/video_data/input_dir
mkdir Yolov7/video_data/output_frames
mkdir Yolov7/video_data/output_frames
mkdir Yolov7/video_data/output_emotions
~~~
- Download the following weights for the yolo model to the weights directory by running the following commands.
~~~
mkdir Yolov7/weights
cd Yolov7/weights
wget https://storage.googleapis.com/edaa_bucket/yolo_weights/face.pt
wget https://storage.googleapis.com/edaa_bucket/yolo_weights/emotions.pt
~~~
- create the following folders inside the preprocessor folder. We couldn't add this here as github does not save empty folders.
~~~
mkdir preprocessor/chunks
mkdir preprocessor/audio
~~~
- run all the other containers
~~~
cd preprocessor
sh docker-shell.sh
cd OpenAI-ASR
sh docker-shell.sh
cd sbert
sh docker-shell.sh
~~~
- Now use the Virtual machines ip address and open the app in browser
 
