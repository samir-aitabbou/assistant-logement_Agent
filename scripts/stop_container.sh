#!/bin/bash

CONTAINER_NAME="assistant-logement-container"

if docker ps -a --format '{{.Names}}' | grep -Eq "^${CONTAINER_NAME}\$"; then
    echo "🛑 Arrêt et suppression du conteneur : $CONTAINER_NAME"
    docker rm -f $CONTAINER_NAME
else
    echo "ℹ️ Aucun conteneur nommé $CONTAINER_NAME n'est en cours."
fi
