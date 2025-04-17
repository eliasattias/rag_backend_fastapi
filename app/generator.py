import os
import requests
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_CHAT_URL = "https://api.mistral.ai/v1/chat/completions"

def generate_answer(query: str, chunks: list) -> str:
    if not chunks:
        return "I couldn't find anything relevant in the uploaded documents."

    context = "\n\n".join(chunks)
    prompt = [
        {"role": "system", "content": "You answer questions based only on the context provided."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-small",
        "messages": prompt,
        "temperature": 0.2
    }

    try:
        res = requests.post(MISTRAL_CHAT_URL, json=payload, headers=headers)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[ERROR] Mistral API call failed: {e}"

