#!/bin/bash

# Testing
echo "Deploy Docker image | Docker Notifier"
# exit 0

# Check if a tag is provided
if [ -z "$1" ]; then
  echo "No tag provided. Exiting deployment."
  exit 1
fi

TAG=$1

# Variables
REGISTRY_ADDRESS="registry.rahpoo.ir"
IMAGE_NAME="docker-notifier"
CONTAINER_NAME="docker-notifier"

# Pull the image with the specified tag
echo "Pulling the image from ${REGISTRY_ADDRESS}/${IMAGE_NAME}:${TAG}..."
docker pull ${REGISTRY_ADDRESS}/${IMAGE_NAME}:${TAG}

# Stop and remove the previous container if it exists
if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
    echo "Stopping and removing the existing container ${CONTAINER_NAME}..."
    docker stop ${CONTAINER_NAME}
    docker rm ${CONTAINER_NAME}
fi

# Remove unused images to save space
echo "Removing unused Docker images..."
docker images -q ${REGISTRY_ADDRESS}/${IMAGE_NAME} | xargs docker rmi -f

# Run the new container
echo "Starting a new container from the image ${REGISTRY_ADDRESS}/${IMAGE_NAME}:${TAG}..."
docker run -d \
    -e HOST_NAME="Amirhosseins_MacBookPro" \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --restart always \
    --name ${CONTAINER_NAME} \
    ${REGISTRY_ADDRESS}/${IMAGE_NAME}:${TAG}

echo "Deployment completed successfully."
