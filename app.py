import streamlit as st
from ui.layout import setup_page_style
from services.rag import rag_repond
from config.constants import MODEL_OPTIONS

def main():
    setup_page_style()
    st.title("🏠 Assistant Logement SCASC")

    st.markdown("## 1. Choisissez votre moteur et modèle")

    # Étape 1 : Choix du moteur
    moteur = st.selectbox("🧠 Moteur de génération :", options=list(MODEL_OPTIONS.keys()))

    # Étape 2 : Choix du modèle correspondant au moteur
    if moteur:
        modeles_disponibles = MODEL_OPTIONS.get(moteur, [])
        modele = st.selectbox("📦 Modèle :", options=modeles_disponibles)
    else:
        modele = None

    st.markdown("---")

    if modele:
        st.markdown("## 2. Posez votre question sur l’aide au logement")
        question = st.text_input("❓ Votre question")

        if st.button("🚀 Obtenir une réponse"):
            if question.strip():
                with st.spinner("🧠 Recherche en cours..."):
                    reponse = rag_repond(
                        question=question,
                        moteur=moteur,
                        modele=modele
                    )
                    st.success("✅ Réponse :")
                    st.markdown(reponse)
            else:
                st.warning("⚠️ Merci de poser une question avant de continuer.")

if __name__ == "__main__":
    main()
