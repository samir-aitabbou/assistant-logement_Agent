


import streamlit as st

def setup_page_style():
    # Configuration de la page
    # st.set_page_config(
    #     page_title='Assistant Logement SCASC',
    #     page_icon='🏠',
    #     layout='centered'
    # )

    # Style personnalisé en HTML/CSS
    custom_css = """
        <style>
            .reportview-container {
                background-color: #f8f9fa;
            }
            .stTextInput > div > div > input {
                border-radius: 10px;
                padding: 10px;
                border: 1px solid #ced4da;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
