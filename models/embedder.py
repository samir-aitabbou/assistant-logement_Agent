# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.9

import faiss
import json
import streamlit as st
from sentence_transformers import SentenceTransformer

def get_embedder():
    return SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

get_embedder = st.cache_resource(get_embedder)

def load_faiss():
    index = faiss.read_index('data/faiss_index.index')
    with open('data/faiss_metadata.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    return (index, metadata)

load_faiss = st.cache_resource(load_faiss)
