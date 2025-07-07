# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: /home/samir.ait-abbou/Bureau/assistant-logement/models/api_models.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 2025-06-25 13:09:08 UTC (1750856948)

import streamlit as st
import google.generativeai as genai
from config.constants import gemini_api_key

@st.cache_resource
def load_api_model(api_choice):
    if api_choice == 'Gemini 1.5 Flash':
        genai.configure(api_key=gemini_api_key)
        return genai.GenerativeModel(model_name='models/gemini-1.5-flash-latest')