#!/bin/bash

# Nom du conteneur
CONTAINER_NAME="assistant-logement-container"
IMAGE_NAME="assistant-logement"
PORT=8501

# Supprimer l'ancien conteneur s'il existe
if docker ps -a --format '{{.Names}}' | grep -Eq "^${CONTAINER_NAME}\$"; then
    echo "🗑️ Suppression de l'ancien conteneur..."
    docker rm -f $CONTAINER_NAME
fi

echo "🚀 Lancement du conteneur Docker : $CONTAINER_NAME"
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8501 \
    -v $(pwd)/data:/app/data \
    -v $(pwd)/outputs:/app/outputs \
    --env-file .env \
    $IMAGE_NAME \
    bash scripts/run.sh
