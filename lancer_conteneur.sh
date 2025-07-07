# Nom du conteneur
CONTAINER_NAME="assistant-logement"
IMAGE_NAME="assistant-logement"
PORT=8601

# Vérifier si le token est défini
if [ -z "$HF_TOKEN" ]; then
    read -sp "Entrez votre Hugging Face Token: " HF_TOKEN
    echo
fi

echo "🚀 Démarrage du conteneur Docker : $CONTAINER_NAME"

# Vérifier si le conteneur est déjà en cours d'exécution
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "🛑 Le conteneur $CONTAINER_NAME est déjà en cours d'exécution. Arrêt..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Lancer le conteneur avec les options appropriées et la variable d'environnement
docker run -d -p $PORT:8501 -v $(pwd)/outputs:/app/outputs --name $CONTAINER_NAME \
    -e HF_TOKEN="$HF_TOKEN" $IMAGE_NAME

# Vérifier si le conteneur a bien démarré
if [ $? -eq 0 ]; then
    echo "✅ Le conteneur $CONTAINER_NAME est lancé avec succès."
    echo "🌐 Accédez à l'application à l'adresse : http://localhost:$PORT"
else
    echo "❌ Échec du démarrage du conteneur. Vérifiez les erreurs ci-dessus."
fi
