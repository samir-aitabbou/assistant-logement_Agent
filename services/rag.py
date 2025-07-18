import streamlit as st
from models.embedder import get_embedder, load_faiss
from models.local_models import load_local_model
from models.api_models import load_api_model
import json
# Initialisation de l'embedder et du moteur de recherche FAISS
embedder = get_embedder()
index, metadata = load_faiss()


def rag_repond(question: str, moteur: str = 'local', modele: str = 'Mistral-7B', top_k: int = 3, seuil_similarite: float = 0.5) -> str:
    question_contextualisee = f'Question sur l’aide au logement : {question}'

    query_vec = embedder.encode([question_contextualisee]).astype('float32')
    distances, indices = index.search(query_vec, top_k)
    meilleure_distance = distances[0][0]
    score_similarite = 1 / (1 + meilleure_distance)

    st.markdown(
        f"<div style='color:gray'><b>🔍 Score de similarité estimée : `{score_similarite:.2f}`</b></div>",
        unsafe_allow_html=True
    )

    if score_similarite < seuil_similarite:
        return (
            "Je suis désolé, je ne peux répondre qu’aux questions liées à l’aide au logement, "
            "selon les informations officielles du SCASC."
        )

    contexte = '\n\n'.join(metadata[i]['contenu'] for i in indices[0])

    if moteur == 'local':
        model_pipeline = load_local_model(modele)
        prompt = (
            f"Tu es un assistant administratif expert en aides sociales. "
            f"En te basant uniquement sur les informations suivantes :\n{contexte}\n\n"
            f"Réponds de façon claire et professionnelle à la question suivante :\n{question}\n\nRéponse :"
        )

        reponse_modele = model_pipeline(prompt)

        # Debug Streamlit + terminal
        st.code(reponse_modele, language="text")
        print("=== Réponse brute du modèle ===")
        print(reponse_modele)

        return reponse_modele.split("Réponse :")[-1].strip()



    if moteur == 'api':
        model_api = load_api_model(modele)
        prompt = (
            f"Tu es un assistant administratif expert en aides sociales. "
            f"Voici des documents de référence officiels :\n{contexte}\n\n"
            f"Réponds de façon claire et professionnelle à la question suivante :\n{question}"
        )
        response = model_api.generate_content(prompt)
        return response.text.strip()