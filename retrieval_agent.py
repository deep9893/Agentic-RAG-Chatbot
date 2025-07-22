# retrieval_agent.py

import faiss
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from mcp import create_mcp

# Load HuggingFace Embedding Model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def build_vector_store(content):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([content])
    db = FAISS.from_documents(docs, embedding)
    return db

def retrieve_context(db, query):
    results = db.similarity_search(query, k=3)
    chunks = [doc.page_content for doc in results]
    return create_mcp("RetrievalAgent", "LLMResponseAgent", "RETRIEVAL_RESULT", {
        "retrieved_context": chunks,
        "query": query
    })
