#!/bin/bash

echo "📦 Vérification de l'installation de Ollama..."

if ! command -v ollama &> /dev/null; then
    echo "🔧 Ollama n'est pas installé. Installation en cours..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama est déjà installé."
fi

echo "🚀 Lancement du service Ollama en arrière-plan..."
pkill ollama 2> /dev/null  # On tue l'ancien processus s'il existe
ollama serve &

sleep 3

# Modèles à préparer
MODELS=("mistral" "nous-hermes2" "tinyllama")

for MODEL in "${MODELS[@]}"; do
    echo "📥 Téléchargement du modèle : $MODEL"
    ollama pull $MODEL
done

echo "✅ Installation terminée. Ollama est prêt avec tous les modèles."
