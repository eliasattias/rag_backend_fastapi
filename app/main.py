from fastapi import FastAPI, UploadFile, File
from typing import List
from app.ingestion import process_pdf_uploads
from app.query_processor import handle_query

app = FastAPI()

@app.post("/ingest")
async def ingest_pdfs(files: List[UploadFile] = File(...)):
    chunks = await process_pdf_uploads(files)
    return {"status": "success", "chunks_stored": chunks}

@app.post("/query")
async def query_endpoint(query: str):
    return handle_query(query)
