# ingestion_agent.py
from utils import *
from mcp import create_mcp

def ingest_file(filepath):
    if filepath.endswith(".pdf"):
        content = extract_text_from_pdf(filepath)
    elif filepath.endswith(".docx"):
        content = extract_text_from_docx(filepath)
    elif filepath.endswith(".csv"):
        content = extract_text_from_csv(filepath)
    elif filepath.endswith(".pptx"):
        content = extract_text_from_pptx(filepath)
    elif filepath.endswith(".txt") or filepath.endswith(".md"):
        content = extract_text_from_txt(filepath)
    else:
        raise ValueError("Unsupported file format")
    
    return create_mcp("IngestionAgent", "RetrievalAgent", "DOC_PARSED", {"content": content})
