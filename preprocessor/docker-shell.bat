
docker network inspect app-network >/dev/null 2>&1 || docker network create app-network
docker build -t preprocessor .
docker run --rm -it -p 8002:8002 --network app-network preprocessor 