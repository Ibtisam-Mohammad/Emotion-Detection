docker network inspect app-network >/dev/null 2>&1 || docker network create app-network
docker build -t yolo .
docker run --rm -it -p 9000:9000 --network app-network --mount type=bind,source="%cd%",target=/app --name yolo yolo