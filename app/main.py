from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=2)
    top_k: int = Field(default=3, ge=1, le=10)


faq_path = Path(__file__).resolve().parent.parent / "data" / "faq.csv"
faq_df = pd.read_csv(faq_path)
faq_df["text"] = faq_df["question"].fillna("") + " " + faq_df["answer"].fillna("")
vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform(faq_df["text"])

app = FastAPI(title="Semantic FAQ Retriever", version="1.0.0")


@app.get("/")
def root() -> dict:
    return {"message": "Semantic FAQ Retriever", "docs": "/docs"}


@app.post("/search")
def search(payload: QueryRequest) -> dict:
    query_vec = vectorizer.transform([payload.query])
    scores = cosine_similarity(query_vec, matrix).flatten()
    ranked = scores.argsort()[::-1][: payload.top_k]

    results = []
    for idx in ranked:
        row = faq_df.iloc[idx]
        results.append(
            {
                "id": int(row["id"]),
                "question": row["question"],
                "answer": row["answer"],
                "domain": row["domain"],
                "score": round(float(scores[idx]), 4),
            }
        )

    return {"query": payload.query, "results": results}


@app.post("/embed")
def embed(payload: QueryRequest) -> dict:
    vec = vectorizer.transform([payload.query]).toarray()[0]
    return {"dimensions": len(vec), "preview": vec[:10].tolist()}
