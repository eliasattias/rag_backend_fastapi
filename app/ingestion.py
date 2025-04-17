import os
import uuid
from fastapi import UploadFile
from app.utils import extract_text_from_pdf, chunk_text, save_chunk

PDF_DIR = "data/pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

async def process_pdf_uploads(files):
    total_chunks = 0
    for file in files:
        contents = await file.read()
        file_id = uuid.uuid4().hex
        path = os.path.join(PDF_DIR, f"{file_id}_{file.filename}")
        with open(path, "wb") as f:
            f.write(contents)

        text = extract_text_from_pdf(path)
        chunks = chunk_text(text)
        for chunk in chunks:
            save_chunk(chunk, file.filename)
        total_chunks += len(chunks)
    return total_chunks
