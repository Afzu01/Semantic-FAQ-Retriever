# Semantic FAQ Retriever

I built this project as a lightweight semantic search backend for FAQ data using TF-IDF embeddings and cosine similarity.

## Features

- Semantic FAQ search endpoint
- Embedding preview endpoint
- Domain-tagged FAQ dataset
- FastAPI docs for quick demo and validation

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

## Why this project helps internship applications

- Demonstrates domain-specific embedding extraction workflow
- Shows practical retrieval implementation with ML libraries
- Easy to explain in interviews with clear architecture
