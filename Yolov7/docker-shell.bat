docker network inspect app-network >/dev/null 2>&1 || docker network create app-network
docker pull us-west2-docker.pkg.dev/mercurial-snow-363512/yolo-repo/yolo-image:tag1
docker run --rm -it -p 9000:9000 --network app-network --mount type=bind,source="%cd%",target=/app --name yolo us-west2-docker.pkg.dev/mercurial-snow-363512/yolo-repo/yolo-image:tag1