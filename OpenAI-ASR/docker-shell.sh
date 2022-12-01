#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Create a network
docker network inspect app-network >/dev/null 2>&1 || docker network create app-network


# Run the container
sudo docker run --rm -it -p 8080:8080 -d --network app-network --mount type=bind,source="$(pwd)",target=/app --name asr us-west2-docker.pkg.dev/mercurial-snow-363512/asr-repo/asr-image
