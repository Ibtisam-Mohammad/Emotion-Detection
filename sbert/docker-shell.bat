docker network inspect app-network >/dev/null 2>&1 || docker network create app-network
docker build -t sbert .
docker run --rm -it -p 8003:8003 --network app-network --mount type=bind,source="%cd%",target=/code/app --name sbert sbert