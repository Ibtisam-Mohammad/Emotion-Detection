docker network inspect app-network >/dev/null 2>&1 || docker network create app-network
docker build -t preprocessor .
docker run --rm -it -p 8005:8005 --network app-network --mount type=bind,source="%cd%",target=/code/app --name preprocessor preprocessor