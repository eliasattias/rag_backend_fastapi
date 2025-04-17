from app.utils import is_small_talk, load_all_chunks
from app.generator import generate_answer

def handle_query(query: str):
    if is_small_talk(query):
        return {"answer": "Hello! How can I help you with the documents?"}

    top_chunks = search_chunks(query)
    answer = generate_answer(query, top_chunks)
    return {"answer": answer}

def search_chunks(query, top_k=3):
    chunks = load_all_chunks()
    ranked = sorted(chunks, key=lambda c: query.lower() in c["text"].lower(), reverse=True)
    return [c["text"] for c in ranked[:top_k]]
