from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.utils import *
from backend.rag import store_document, query_documents
from backend.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"message": "Welcome to RAG + Azure LLM"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    name = file.filename
    ext = name.split(".")[-1].lower()

    if ext == "pdf":
        content = extract_text_from_pdf(contents)
    elif ext in ["jpg", "jpeg", "png"]:
        content = extract_text_from_image(contents)
    elif ext == "docx":
        content = extract_text_from_docx(contents)
    elif ext == "txt":
        content = contents.decode("utf-8")
    else:
        return {"error": "Unsupported file format"}

    store_document(name, content)
    return {"message": f"✅ Document '{name}' uploaded and indexed."}

@app.get("/query")
def get_answer(q: str):
    answer = query_documents(q)
    return {"answer": answer}