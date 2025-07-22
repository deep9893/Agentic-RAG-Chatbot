# app.py
import streamlit as st
from ingestion_agent import ingest_file
from retrieval_agent import build_vector_store, retrieve_context
from llm_response_agent import generate_answer

st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
st.title("🧠 Agentic RAG Chatbot")

if "db" not in st.session_state:
    st.session_state.db = None

uploaded_file = st.file_uploader("📄 Upload a document", type=["pdf", "docx", "csv", "pptx", "txt", "md"])
if uploaded_file:
    with open(f"temp_{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
    mcp_doc = ingest_file(f"temp_{uploaded_file.name}")
    st.session_state.db = build_vector_store(mcp_doc["payload"]["content"])
    st.success("Document processed and indexed!")

query = st.text_input("💬 Ask your question")
if query and st.session_state.db:
    mcp_query = retrieve_context(st.session_state.db, query)
    answer = generate_answer(mcp_query)
    st.write("📝 **Answer:**", answer)
