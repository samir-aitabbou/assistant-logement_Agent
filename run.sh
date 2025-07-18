#!/bin/bash

# Rendre le script d'installation exécutable
chmod +x install_ollama.sh

# ✅ Exécuter l'installation de Ollama + modèles
./install_ollama.sh

# 🧪 Vérifie que Streamlit est bien installé
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit n'est pas installé. Activation de l'environnement virtuel..."
    source .venv/bin/activate
    pip install -r requirements.txt
fi

# 🚀 Lancer l'application Streamlit
echo "🚀 Démarrage de l'application Streamlit..."
streamlit run app.py


# streamlit run app.py --server.address=0.0.0.0 --server.port=8502
