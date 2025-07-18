


import streamlit as st

def setup_page_style():
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
