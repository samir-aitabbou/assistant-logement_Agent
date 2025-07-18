# models/api_models.py
# This module provides functionality to load API models for text generation.
# It uses Google Generative AI for generating responses based on prompts.

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis la variable d'environnement
gemini_api_key = os.getenv("GEMINI_API_KEY")

@st.cache_resource
def load_api_model(api_choice):
    if api_choice == 'Gemini 1.5 Flash':
        genai.configure(api_key=gemini_api_key)
        return genai.GenerativeModel(model_name='models/gemini-1.5-flash-latest')
