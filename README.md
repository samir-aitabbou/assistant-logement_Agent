
# 🏠 Assistant Logement SCASC

> Un assistant intelligent qui répond aux questions liées aux aides au logement en utilisant des modèles de génération de texte (locaux via Ollama ou via API Gemini) et la méthode RAG (Retrieval-Augmented Generation).

---

## 📂 Structure du projet

```
assistant-logement/
│
├── app.py                      # Script principal Streamlit
├── run.sh                      # Script de démarrage automatisé (Ollama + Streamlit)
├── install_ollama.sh           # Script d'installation d'Ollama + modèles
├── config/
│   └── constants.py             # Clé API et modèles disponibles
├── models/
│   ├── api_models.py            # Chargement des modèles via API (Gemini)
│   ├── local_models.py          # Chargement des modèles locaux (via Ollama)
│   └── embedder.py              # Embedder + FAISS loader
├── services/
│   └── rag.py                   # Logique RAG principale
├── utils/
│   └── device.py                # Détection GPU ou CPU
├── ui/
│   └── layout.py                # Configuration visuelle de l’app
├── data/
│   ├── faiss_index.index        # Index vectoriel FAISS
│   └── faiss_metadata.json      # Métadonnées associées aux documents
├── README.md                    # Ce fichier
└── requirements.txt             # Dépendances Python
```

---

## 🚀 Fonctionnalités

- 🔍 Récupération intelligente des documents pertinents via FAISS
- 🧠 Génération de texte par modèle local (`Mistral`, `Nous Hermes`, etc.) via **Ollama**
- 🌐 Génération par API (`Gemini`)
- 💬 Interface simple via Streamlit
- 📊 Affichage du score de similarité
- 🔌 Mode GPU/CPU détecté automatiquement

---

## 🎥 Aperçu de l'application

<p align="center">
  <img src="./docs/assistant_logement.gif" alt="Démo de l'application" />
</p>

---


## ⚙️ Prérequis

- Python 3.9+
- GPU (optionnel mais recommandé pour Ollama)
- [Ollama](https://ollama.com) (installé automatiquement)

---

## 📦 Installation

```bash
# 1. Clone du repo
git clone https://gitlab.cedre.univ-amu.fr/samir.ait-abbou/assistant-logement.git
cd assistant-logement

# 2. Création de l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 3. Installation des dépendances Python
pip install --upgrade pip
pip install -r requirements.txt

# 4. Lancement automatique d'Ollama + modèles + Streamlit
./run.sh
```

---

### ⚠️ Note importante lors du premier lancement

> Lors du premier lancement via le script `run.sh`, le système va installer **Ollama** s’il n’est pas déjà présent.

🛠️ Cette installation utilise le script officiel `https://ollama.com/install.sh`, et :

- 💡 **Le terminal peut vous demander de saisir votre mot de passe** (commande `sudo`) pour autoriser l'installation dans le système (`/usr/local`).
- ✅ C'est une procédure normale et sécurisée.
- 📌 **Aucune confirmation manuelle n'est demandée pour télécharger les modèles.**

🔔 **Merci de bien surveiller le terminal pendant cette étape.**

---

---

### 🪟 Utilisation sous WSL (Windows Subsystem for Linux)

Si vous utilisez WSL (par exemple Ubuntu sous Windows), vous pourriez voir ce message lors de l’installation d’Ollama :

Cela signifie que le service Ollama ne peut pas démarrer automatiquement via `systemd`.

✅ Dans ce cas, lancez simplement le serveur Ollama manuellement :

```bash
ollama serve &
```
-----

💡 Pour une solution permanente, vous pouvez activer systemd dans WSL : https://learn.microsoft.com/en-us/windows/wsl/systemd#how-to-enable-systemd



## 🔐 Configuration

### Clé API Gemini

Créer un fichier `.env` à la racine du projet (exemple dans `example.env`) :

```
GEMINI_API_KEY=AIza...
```

---

## 🧠 Téléchargement des modèles locaux via Ollama

Les modèles suivants sont téléchargés **automatiquement** au premier lancement :

- `mistral` (Mistral-7B-Instruct)
- `nous-hermes2` (Nous Hermes 2 - Mistral)
- `tinyllama` (TinyLlama 1.1B)

✅ Aucune action manuelle requise  
✅ Pas de compte Hugging Face  
✅ Compatible CPU/GPU automatiquement

---

## 📁 Données RAG

Le dossier `data/` doit contenir :

- `faiss_index.index` : index vectoriel
- `faiss_metadata.json` : documents liés

Si ces fichiers n'existent pas, tu peux les générer avec FAISS + SentenceTransformer sur tes documents.

---

## ▶️ Lancement de l’app (manuel)

```bash
# Si tu veux lancer manuellement
./install_ollama.sh      # Installe Ollama + les modèles
streamlit run app.py     # Lance l'app
```

---

## 🧪 Exemple d'utilisation

1. Choisir `local` ou `api`
2. Choisir le modèle (`Mistral`, `Nous Hermes`, `Gemini`, etc.)
3. Taper une question comme :  
   > "Puis-je bénéficier d'aide au logement ?"
4. Obtenir une réponse issue de documents officiels

---

## 🛠️ Dépendances principales

- `streamlit`
- `requests`
- `sentence-transformers`
- `faiss-cpu`
- `google-generativeai`

---
