# Étape 1: Utiliser une image de base légère avec Python
FROM python:3.10-slim

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de configuration et le script principal
COPY app.py /app/
COPY environment_linux.yml /app/
COPY environment_mac.yml /app/
COPY outputs /app/outputs/

# Copier le fichier de requirements commun
COPY requirements.txt /app/

# Installer les packages nécessaires pour Hugging Face
RUN pip install --no-cache-dir transformers huggingface-hub

# Installer pip
RUN pip install --no-cache-dir pip setuptools wheel

# Installation des dépendances via pip
RUN pip install -r /app/requirements.txt

# Exposer le port pour Streamlit
EXPOSE 8501

# Lancer l'application Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
