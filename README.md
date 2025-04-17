# Retrieval-Augmented Generation (RAG) Backend

A lightweight Python backend implementing a Retrieval-Augmented Generation (RAG) system using FastAPI and the Mistral AI API.

This project allows you to:
- Upload PDF documents to build a knowledge base.
- Ask natural language questions.
- Receive answers grounded in the uploaded content using Mistral LLM.

## 📂 Folder Structure
```
rag_pipeline/
├── app/
│   ├── main.py               # FastAPI app with endpoints
│   ├── ingestion.py          # PDF upload, text extraction, chunking
│   ├── query_processor.py    # Intent detection, keyword search
│   ├── generator.py          # LLM query handler using Mistral API
│   └── utils.py              # Text extraction, chunk management
├── data/
│   ├── pdfs/                 # Uploaded PDF files
│   └── chunks/               # Stored text chunks (JSON format)
├── .env                      # Mistral API key
├── requirements.txt
├── README.md
└── .gitignore
```

## ✅ Features
- Upload one or more PDFs using `/ingest`
- Extracts text and breaks it into overlapping chunks
- Answers questions using Mistral AI's `mistral-small` model
- No external vector databases or libraries (pure Python)

## ⚙️ How It Works

### Ingestion Flow (`/ingest`)
1. User uploads PDF(s)
2. Text is extracted using PyMuPDF
3. Text is chunked into 300-word segments with overlap
4. Each chunk is saved locally as a JSON file

### Query Flow (`/query`)
1. User asks a question
2. If it’s a greeting, return a canned response
3. Else, search all saved chunks using keyword matching
4. Pass top relevant chunks + query to Mistral LLM
5. Return the generated answer

### System Diagram
```
User
  |
  |---[POST /ingest]---> PDF Text Extraction & Chunking
  |                          |
  |                          --> Store chunks in /data/chunks/
  |
  |---[POST /query]----> Intent Detection
                             |
                             --> Keyword Search on chunks
                             --> Select Top Chunks
                             --> Call Mistral API with context
                             --> Return Generated Answer
```

## ▶️ Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/eliasattias/rag_backend_fastapi.git
cd rag-pipeline
```

### 2. Set up your environment
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add `.env`
```
MISTRAL_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
uvicorn app.main:app --reload
```
Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5. Test the endpoints
- Upload PDFs at `/ingest`
- Ask questions at `/query`

## 📚 Libraries Used
- [FastAPI](https://fastapi.tiangolo.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz`) for PDF parsing
- [Mistral AI API](https://docs.mistral.ai) for answer generation
- [python-dotenv](https://pypi.org/project/python-dotenv/) for config

## ✅ Evaluation Criteria
- No external RAG libraries used
- No vector DB
- All logic implemented manually with clean modular code
- To keep within the scope of no external libraries or vector DBs, this implementation uses keyword matching. A future enhancement would compute semantic similarity using LLM output embeddings

---

## 📬 Contact
Elias Attias  
attiaselias@gmail.com