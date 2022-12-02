#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Create a network
sudo docker network inspect app-network >/dev/null 2>&1 || docker network create app-network

# Build the image based on the Dockerfile
sudo docker build -t frontend .

# Run the container
sudo docker run -it --rm --name frontend -p 3000:3000 --mount type=bind,source="$(pwd)",target=/react_app --network app-network frontend