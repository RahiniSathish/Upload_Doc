 **Document Upload Chatbot (RAG + LLM)**
A powerful AI-powered chatbot that allows users to upload documents (PDF, DOCX, TXT, Images) and ask questions. The system uses OCR for images, extracts tables/charts/text, stores it in a vector database, and answers questions using a Large Language Model (LLM).

---

## Features

- Upload documents in `.pdf`, `.docx`, `.txt`, `.jpg`, `.png`
- Extracts content including:
  -  Raw text
  -  Tables
  -  Text from images (OCR via Tesseract)
-  Indexes content into a vector database (Chroma/FAISS/SQL)
-  Uses **Azure OpenAI** (or any LLM) for contextual Q&A
-  Memory-aware, intelligent responses using RAG pipeline
-  Ask natural questions from uploaded content

---

##  How It Works

1. Upload a document (text, scanned, or formatted).
2. Backend processes and extracts content.
3. Splits and stores it in vector format.
4. You ask a question → it retrieves relevant parts → sends to LLM.
5. LLM generates an accurate, context-aware answer.



##  Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Document Processing**: PyMuPDF, python-docx, pytesseract
- **Vector DB**: Chroma (or replaceable with FAISS, Pinecone)
- **LLM**: Azure OpenAI (via LangChain)
- **OCR**: Tesseract for image-based documents
- **Database**: SQLite (or can plug-in PostgreSQL)
