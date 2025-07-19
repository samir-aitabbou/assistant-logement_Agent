#!/bin/bash

# export TMPDIR=$HOME/.podman-tmp
# mkdir -p "$TMPDIR"

CONTAINER_NAME="assistant-logement-container"
IMAGE_NAME="assistant-logement"
PORT=8501

# Vérifier si le conteneur existe
if docker ps -a --format '{{.Names}}' | grep -Eq "^${CONTAINER_NAME}\$"; then
    echo "⏹️  Arrêt du conteneur existant..."
    docker stop $CONTAINER_NAME

    echo "🗑️  Suppression de l'ancien conteneur..."
    docker rm $CONTAINER_NAME
fi

echo "🚀 Lancement du conteneur Docker : $CONTAINER_NAME"
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8501 \
    -v "$(pwd)/data:/app/data" \
    --env-file .env \
    $IMAGE_NAME \
    bash scripts/run.sh
