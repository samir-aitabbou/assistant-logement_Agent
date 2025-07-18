#!/bin/bash

# Rendre install_ollama exécutable et l’exécuter
chmod +x scripts/install_ollama.sh
./scripts/install_ollama.sh

# Vérifier et installer Streamlit si besoin
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit n'est pas installé. Installation..."
    pip install -r requirements.txt
fi

# Démarrer Streamlit
echo "🚀 Démarrage de l'application Streamlit..."
streamlit run app.py






