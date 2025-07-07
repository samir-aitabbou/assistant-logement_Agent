# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: /home/samir.ait-abbou/Bureau/assistant-logement/services/rag.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 2025-06-25 12:56:47 UTC (1750856207)



import streamlit as st
from models.embedder import get_embedder, load_faiss
from models.local_models import load_local_model
from models.api_models import load_api_model

# Initialisation de l'embedder et du moteur de recherche FAISS
embedder = get_embedder()
index, metadata = load_faiss()

def rag_repond(question: str, moteur: str = 'local', modele: str = 'Mistral-7B', top_k: int = 3, seuil_similarite: float = 0.5) -> str:
    """
    Répond à une question en utilisant la méthode RAG (Retrieval-Augmented Generation).
    
    Args:
        question (str): La question posée par l'utilisateur.
        moteur (str): Choix du moteur de génération ('local' ou 'api').
        modele (str): Nom du modèle à utiliser.
        top_k (int): Nombre de documents les plus similaires à récupérer.
        seuil_similarite (float): Seuil minimal de similarité pour répondre.

    Returns:
        str: La réponse générée ou un message d'erreur si la similarité est trop faible.
    """
    # Ajouter un contexte spécifique au sujet logement
    question_contextualisee = f'Question sur l’aide au logement : {question}'

    # Encodage de la question en vecteur
    query_vec = embedder.encode([question_contextualisee]).astype('float32')

    # Recherche des top_k documents les plus proches
    distances, indices = index.search(query_vec, top_k)

    # Calcul du score de similarité à partir de la plus proche distance
    meilleure_distance = distances[0][0]
    score_similarite = 1 / (1 + meilleure_distance)

    # Affichage du score dans Streamlit
    st.markdown(
        f"<div style='color:gray'><b>🔍 Score de similarité estimée : `{score_similarite:.2f}`</b></div>",
        unsafe_allow_html=True
    )

    # Vérification du seuil de similarité
    if score_similarite < seuil_similarite:
        return (
            "Je suis désolé, je ne peux répondre qu’aux questions liées à l’aide au logement, "
            "selon les informations officielles du SCASC."
        )

    # Construction du contexte textuel à partir des documents récupérés
    contexte = '\n\n'.join(metadata[i]['contenu'] for i in indices[0])

    # Choix du moteur local pour la génération de texte
    if moteur == 'local':
        model_pipeline = load_local_model(modele)
        prompt = (
            f"Tu es un assistant administratif expert en aides sociales. "
            f"En te basant uniquement sur les informations suivantes :\n{contexte}\n\n"
            f"Réponds de façon claire et professionnelle à la question suivante :\n{question}\n\nRéponse :"
        )
        resultat = model_pipeline(prompt)[0]['generated_text']
        # Extraction de la réponse après "Réponse :"
        return resultat.split('Réponse :')[-1].strip()

    # Choix du moteur API pour la génération
    if moteur == 'api':
        model_api = load_api_model(modele)
        prompt = (
            f"Tu es un assistant administratif expert en aides sociales. "
            f"Voici des documents de référence officiels :\n{contexte}\n\n"
            f"Réponds de façon claire et professionnelle à la question suivante :\n{question}"
        )
        response = model_api.generate_content(prompt)
        return response.text.strip()
