import os
import uuid
import fitz  # PyMuPDF
import json

CHUNK_DIR = "data/chunks"
os.makedirs(CHUNK_DIR, exist_ok=True)

def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    return "".join(page.get_text() for page in doc).strip()

def chunk_text(text: str, size: int = 300, overlap: int = 50):
    '''
    We chunk text into 300-word segments with 50-word overlap
    to preserve context across boundaries and prevent loss of 
    meaning when splitting paragraphs.'''
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size - overlap)]

def save_chunk(text: str, source: str):
    data = {
        "id": uuid.uuid4().hex,
        "source": source,
        "text": text
    }
    path = os.path.join(CHUNK_DIR, f"{data['id']}.json")
    with open(path, "w") as f:
        json.dump(data, f)

def load_all_chunks():
    all_chunks = []
    for fname in os.listdir(CHUNK_DIR):
        with open(os.path.join(CHUNK_DIR, fname)) as f:
            all_chunks.append(json.load(f))
    return all_chunks

def is_small_talk(query: str):
    return query.lower().strip() in {"hi", "hello", "hey", "thanks", "bye"}

def transform_query(q):
    return q.strip().lower()
