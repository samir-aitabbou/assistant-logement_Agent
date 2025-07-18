# models/local_models.py
# Local model loading for text generation using Ollama (API locale)
import streamlit as st
import requests
import subprocess
import shutil
import time
from utils.device import detect_device
import json


# MODEL_MAP = {
#     'Mistral-7B': 'mistral',
#     'Gemma-2B': 'gemma:2b',
#     'TinyLlama': 'tinyllama',
#     'LLaMA3-8B': 'llama3:8b'
# }

MODEL_MAP = {
    'Gemma-2B': 'gemma:2b',
}

OLLAMA_API_URL = "http://localhost:11434"

def ensure_ollama_installed():
    """Vérifie si Ollama est installé, sinon propose l'installation."""
    if shutil.which("ollama") is None:
        st.error("❌ Ollama n'est pas installé. Veuillez l'installer manuellement : [https://ollama.com](https://ollama.com)")
        st.stop()

def ensure_ollama_running():
    """Vérifie si le serveur Ollama tourne, sinon le lance en arrière-plan."""
    try:
        requests.get(OLLAMA_API_URL + "/api/tags")
    except requests.exceptions.ConnectionError:
        try:
            subprocess.Popen(["ollama", "serve"])
            time.sleep(3)  # Laisser le temps au serveur de démarrer
        except Exception as e:
            st.error(f"❌ Échec du lancement de Ollama : {e}")
            st.stop()

def pull_model(model_name: str):
    """Tire le modèle s'il n'est pas encore installé localement."""
    response = requests.get(OLLAMA_API_URL + "/api/tags")
    local_models = response.json().get("models", [])
    if not any(m["name"] == model_name for m in local_models):
        with st.spinner(f"📦 Téléchargement du modèle `{model_name}`..."):
            pull = subprocess.run(["ollama", "pull", model_name], capture_output=True, text=True)
            if pull.returncode != 0:
                st.error(f"❌ Erreur lors du téléchargement du modèle :\n{pull.stderr}")
                st.stop()

@st.cache_resource
def load_local_model(model_choice: str):
    """
    Initialise Ollama, vérifie et télécharge le modèle si besoin,
    puis retourne une fonction de génération de texte.
    """
    # Check prerequisites
    ensure_ollama_installed()
    ensure_ollama_running()

    model_name = MODEL_MAP.get(model_choice, MODEL_MAP['Mistral-7B'])
    pull_model(model_name)

    # Affichage de l'état du device
    device = detect_device()
    st.markdown(
        f"<div style='color:green'><b>🚀 Modèle `{model_choice}` prêt via Ollama</b></div>",
        unsafe_allow_html=True
    )
    if device == 'cuda':
        import torch
        gpu_name = torch.cuda.get_device_name(0)
        st.markdown(
            f"<div style='color:blue'><b>🖥️ GPU détecté : `{gpu_name}`</b></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='color:red'><b>⚠️ Aucun GPU détecté. Ollama utilisera le CPU.</b></div>",
            unsafe_allow_html=True
        )

    # def generate_text(prompt: str, model=model_name) -> str:
    #     try:
    #         response = requests.post(
    #             f"{OLLAMA_API_URL}/api/generate",
    #             json={"model": model, "prompt": prompt}
    #         )
    #         return response.json().get("response", "").strip()
    #     except Exception as e:
    #         return f"Erreur lors de la génération : {e}"

    def generate_text(prompt: str, model=model_name) -> str:
        try:
            response = requests.post(
                f"{OLLAMA_API_URL}/api/generate",
                json={"model": model, "prompt": prompt},
                stream=True  # Important pour lecture ligne par ligne
            )

            generated_text = ""

            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        chunk = data.get("response", "")
                        generated_text += chunk
                    except json.JSONDecodeError as e:
                        print("Erreur de parsing JSON (ligne):", line)
                        print("Exception :", e)

            return generated_text.strip()

        except Exception as e:
            print("Erreur lors de la requête vers Ollama :", e)
            return f"Erreur lors de la génération : {e}"


    return generate_text
