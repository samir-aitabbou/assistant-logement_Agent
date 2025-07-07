# # Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# # Version : Python 3.9

import streamlit as st
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    pipeline
)
from utils.device import detect_device

# Dictionnaire des modèles disponibles
MODEL_MAP = {
    'Mistral-7B': 'mistralai/Mistral-7B-Instruct-v0.1',
    'Nous-Hermes-2': 'NousResearch/Nous-Hermes-2-Mistral-7B',
    'TinyLlama': 'TinyLlama/TinyLlama-1.1B-Chat-v1.0'
}

@st.cache_resource
def load_local_model(model_choice: str):
    """
    Charge un modèle de génération de texte depuis Hugging Face selon le choix de l'utilisateur.
    Utilise la détection automatique du GPU (si disponible).
    """
    # Récupération du nom complet du modèle depuis la map
    model_name = MODEL_MAP.get(model_choice, MODEL_MAP['Mistral-7B'])

    # Détection du device (GPU ou CPU)
    device = detect_device()
    st.markdown(
        f"<div style='color:green'><b>🚀 Modèle chargé sur : `{device.upper()}`</b></div>",
        unsafe_allow_html=True
    )

    # Affichage du GPU si disponible
    if device == 'cuda':
        import torch
        gpu_name = torch.cuda.get_device_name(0)
        st.markdown(
            f"<div style='color:blue'><b>🖥️ GPU détecté : `{gpu_name}`</b></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='color:red'><b>⚠️ Aucun GPU détecté. Exécution sur CPU.</b></div>",
            unsafe_allow_html=True
        )

    # Chargement du tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    # Chargement du modèle
    try:
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map='auto',
            torch_dtype='auto'
        )
    except Exception:
        # Fallback forcé sur CPU si échec du chargement GPU
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map={'': 'cpu'},
            torch_dtype='auto'
        )

    # Création du pipeline de génération de texte
    text_gen_pipeline = pipeline(
        'text-generation',
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        do_sample=True
    )

    return text_gen_pipeline
