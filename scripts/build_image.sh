#!/bin/bash

# Nom de l'image
IMAGE_NAME="assistant-logement"

echo "🔨 Construction de l'image Docker : $IMAGE_NAME"
docker build -t $IMAGE_NAME .