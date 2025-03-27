from backend.models import Document
from backend.db import SessionLocal
from backend.llm import get_response

def store_document(name, content):
    db = SessionLocal()
    doc = Document(name=name, content=content)
    db.add(doc)
    db.commit()
    db.close()

def query_documents(question):
    db = SessionLocal()
    docs = db.query(Document).all()
    combined_text = "\n\n".join([d.content for d in docs])
    db.close()

    prompt = f"""Answer the question based on the following documents:
    {combined_text}
    
    Question: {question}
    Answer:"""
    response = get_response(prompt)
    return response.content
