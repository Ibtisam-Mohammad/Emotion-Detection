#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Create a network
docker network inspect app-network >/dev/null 2>&1 || docker network create app-network

# Build the image based on the Dockerfile
#docker build -t yolo .

# Run the container
sudo docker run --rm -it -d -p 9000:9000 --network app-network --mount type=bind,source="$(pwd)",target=/app --name yolo us-west2-docker.pkg.dev/mercurial-snow-363512/yolo-repo/yolo-image:tag1 
