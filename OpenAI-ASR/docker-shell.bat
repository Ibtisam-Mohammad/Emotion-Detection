docker network inspect app-network >/dev/null 2>&1 || docker network create app-network
docker build -t asr .
docker run --rm -it -p 8080:8080 --network app-network --mount type=bind,source="%cd%/",target=/app --name asr asr