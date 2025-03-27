import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
SERVER = f"http://localhost:8000"
st.set_page_config(page_title="Azure RAG Chatbot")
st.title("📄 Upload & Ask")
file = st.file_uploader("Upload txt, pdf, docx, jpg", type=["pdf", "docx", "jpg", "jpeg", "txt", "png"])
if file and st.button("Upload"):
    files = {"file": (file.name, file.getvalue())}
    r = requests.post(f"{SERVER}/upload", files=files)
    st.success(r.json().get("message", "Uploaded."))
query = st.text_input("Ask a question")
if st.button("Ask"):
    r = requests.get(f"{SERVER}/query", params={"q": query})
    st.write("Answer:", r.json().get("answer", "No response."))
