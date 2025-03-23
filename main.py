import sys
import os

# Dynamically add the 'buyogo' root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi import FastAPI
from scripts.query_rag import get_rag_answer
from scripts.analytics import get_analytics



app = FastAPI()

@app.post("/ask")
async def ask_question(query: dict):
    """
    API endpoint to handle user queries using RAG-based retrieval.
    """
    response = get_rag_answer(query["query"])
    return {"answers": response}

@app.post("/analytics")
async def analytics(query: dict):
    """
    API endpoint to provide analytical insights from booking data.
    """
    result = get_analytics(query["query_type"])
    return {"result": result}

@app.get("/")
async def root():
    """
    Health check endpoint.
    """
    return {"message": "LLM-Powered Booking Analytics & QA System is running!"}
