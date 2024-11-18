#!/bin/bash

echo "Build Docker image | Docker Notifier"

NAME="docker-notifier"
IMAGE_NAME="${NAME}:${CI_COMMIT_TAG}"
REGISTRY_ADDRESS="registry.rahpoo.ir"

docker build --platform linux/amd64 -t $IMAGE_NAME .

docker tag $IMAGE_NAME ${REGISTRY_ADDRESS}/$IMAGE_NAME
docker push ${REGISTRY_ADDRESS}/$IMAGE_NAME

docker tag $IMAGE_NAME ${REGISTRY_ADDRESS}/${NAME}:latest
docker push ${REGISTRY_ADDRESS}/${NAME}:latest
