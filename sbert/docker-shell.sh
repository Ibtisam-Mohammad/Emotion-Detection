#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Create a network
docker network inspect app-network >/dev/null 2>&1 || docker network create app-network

# Build the image based on the Dockerfile
docker build -t sbert .

# Run the container
sudo docker run --rm -it -d -p 8003:8003 --network app-network --mount type=bind,source="$(pwd)",target=/code/app --name sbert sbert