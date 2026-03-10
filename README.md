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
uvicorn app.main:app --reload --port 8002
```

Open after startup (local machine only): [http://127.0.0.1:8002/docs](http://127.0.0.1:8002/docs)

UI Demo (local machine only): [http://127.0.0.1:8002/ui](http://127.0.0.1:8002/ui)

## For Recruiters

- Local API docs: http://127.0.0.1:8002/docs
- Live deployment URL: add after deployment
- Suggested screenshots:
	- docs_home.png
	- search_response.png

Sample request
POST /search
{
	"query": "webhook api integration",
	"top_k": 3
}

Sample response
{
	"query": "webhook api integration",
	"results": [
		{
			"id": 3,
			"question": "How to connect webhook to API?",
			"domain": "integrations",
			"score": 0.81
		}
	]
}

## Recruiter Demo Script

Use this exact flow in a live demo:

1. Open `/ui`
2. In search box use: `webhook api integration`
3. Keep `top_k = 3`
4. Click `Run /search`
5. Explain: "The model ranks FAQ items using TF-IDF vectors and cosine similarity."
6. In embedding box use: `how embeddings help retrieval`
7. Click `Run /embed`
8. Explain: "This endpoint returns vector dimensions and preview values for semantic pipelines."

What to highlight while presenting:

- API-first design with FastAPI contracts
- Explainable ranking approach suitable for baseline production use
- Easy path to scale into transformer embeddings and vector databases

## Future Improvements

- Add persistent storage for larger FAQ collections
- Add query logging and analytics for relevance tuning
- Upgrade to a hybrid retrieval strategy for better ranking quality
