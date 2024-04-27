#!/bin/bash

# Check if Docker is already installed
if ! command -v docker &> /dev/null; then
    # Install Docker
    sudo apt-get update
    sudo apt-get install -y docker.io
    echo "Docker installed successfully."
else
    echo "Docker is already installed."
fi

# Check if Docker Compose is already installed
if ! command -v docker-compose &> /dev/null; then
    # Install Docker Compose
    sudo apt-get update
    sudo apt-get install -y docker-compose
    echo "Docker Compose installed successfully."
else
    echo "Docker Compose is already installed."
fi

# Check if the folder exists
if [ -d "TheVal-Discord-Bot" ]; then
    echo "TheVal-Discord-Bot repository already exists. Stopping and removing existing Docker containers..."
    # Stop and remove existing Docker containers
    docker-compose -f "TheVal-Discord-Bot/docker-compose.yml" down
else
    # Clone the repository if it doesn't exist
    git clone https://github.com/TheValll/TheVal-Discord-Bot
    cd TheVal-Discord-Bot || exit
    echo "TheVal-Discord-Bot repository cloned successfully."
fi

# Build the Docker image
docker build --pull --rm -f "dockerfile" -t bot:latest "."

# Start the Docker containers
docker-compose -f "docker-compose.yml" up -d --build

echo "TheVal Bot installation completed successfully."