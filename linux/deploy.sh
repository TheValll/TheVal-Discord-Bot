#!/bin/bash

# Install Docker
sudo apt-get update
sudo apt-get install -y docker.io

# Install Docker Compose
sudo apt-get install -y docker-compose

# Check if the folder exists
if [ -d "TheVal-Discord-Bot" ]; then
    echo "Le dossier existe déjà. Arrêt et suppression des conteneurs Docker existants..."
    # Stop and remove existing Docker containers
    docker-compose -f "TheVal-Discord-Bot/docker-compose.yml" down
else
    # Clone the repository if it doesn't exist
    git clone https://github.com/TheValll/TheVal-Discord-Bot
    cd TheVal-Discord-Bot
fi

# Build the Docker image
docker build --pull --rm -f "dockerfile" -t bot:latest "."

# Start the Docker containers
docker-compose -f "docker-compose.yml" up -d --build