# llm_response_agent.py

from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

# Load a lightweight local generation model (e.g. Flan-T5)
qa_model = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)

llm = HuggingFacePipeline(pipeline=qa_model)
chain = load_qa_chain(llm, chain_type="stuff")

def generate_answer(context_mcp):
    context = context_mcp["payload"]["retrieved_context"]
    question = context_mcp["payload"]["query"]

    docs = [Document(page_content=chunk) for chunk in context]
    result = chain.run(input_documents=docs, question=question)
    return result
