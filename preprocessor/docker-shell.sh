#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Create a network
sudo docker network inspect app-network >/dev/null 2>&1 || sudo docker network create app-network

# Build the image based on the Dockerfile
sudo docker build -t preprocessor .

# Run the container
sudo docker run --rm -d -p 8005:8005 --network app-network --mount type=bind,source="$(pwd)",target=/code/app --name preprocessor preprocessor

