FROM python:3.10-slim

# Installer dépendances système
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*

# Installer Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Créer dossier de travail
WORKDIR /app

# Copier uniquement les fichiers utiles
COPY . .

# Installer les dépendances Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Rendre les scripts exécutables
RUN chmod +x scripts/*.sh
 
# Exposer les ports
 # Streamlit
EXPOSE 8501 
# Ollama
EXPOSE 11434  

# Commande par défaut : lance le script complet
CMD ["scripts/run.sh"]
