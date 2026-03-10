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

## Future Improvements

- Add persistent storage for larger FAQ collections
- Add query logging and analytics for relevance tuning
- Upgrade to a hybrid retrieval strategy for better ranking quality
