#!/bin/bash

echo "📦 Vérification de l'installation de Ollama..."

if ! command -v ollama &> /dev/null; then
    echo "🔧 Ollama n'est pas installé. Installation en cours..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama est déjà installé."
fi

echo "🚀 Lancement du service Ollama en arrière-plan..."
pkill ollama 2> /dev/null
ollama serve &

sleep 3

# Liste des modèles à tirer
declare -A MODEL_MAP=(
    # ["Mistral-7B"]="mistral"
    ["Gemma-2B"]="gemma:2b"
    # ["TinyLlama"]="tinyllama"
    # ["LLaMA3-8B"]="llama3:8b"
)

for model_key in "${!MODEL_MAP[@]}"; do
    MODEL="${MODEL_MAP[$model_key]}"
    echo "📥 Téléchargement du modèle : $model_key -> $MODEL"
    ollama pull "$MODEL"
done

echo "✅ Installation terminée. Ollama est prêt avec tous les modèles."
