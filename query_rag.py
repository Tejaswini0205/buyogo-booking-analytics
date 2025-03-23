import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Define paths
BASE_DIR = r"C:\Users\sri tejasw\buyogo"
INDEX_PATH = os.path.join(BASE_DIR, "embeddings", "faiss_index.bin")
METADATA_PATH = os.path.join(BASE_DIR, "embeddings", "metadata.pkl")

# Load FAISS index
print("🚀 Loading FAISS index...")
if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
else:
    raise FileNotFoundError(f"FAISS index file not found: {INDEX_PATH}")

# Load metadata
if os.path.exists(METADATA_PATH):
    with open(METADATA_PATH, "rb") as f:
        metadata = pickle.load(f)
else:
    raise FileNotFoundError(f"Metadata file not found: {METADATA_PATH}")

print("✅ FAISS index and metadata loaded successfully!")

# Load embedding model
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Set up Gemini API
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("❌ Google Gemini API key not found! Set it as an environment variable: GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

# Select Gemini model
MODEL_NAME = "gemini-1.5-pro"  # Change if needed
model = genai.GenerativeModel(MODEL_NAME)
print(f"✅ Using Gemini model: {MODEL_NAME}")

def retrieve_top_k(query_text, k=5):
    """Retrieve top-k similar entries from FAISS index."""
    query_embedding = embedder.encode([query_text])
    _, indices = index.search(query_embedding, k)
    return [metadata[i] for i in indices[0] if i < len(metadata)]

def get_rag_answer(query):
    """Retrieve relevant data and generate an answer using Gemini."""
    print(f"🔍 Query: {query}")

    retrieved_data = retrieve_top_k(query)
    if not retrieved_data:
        return "No relevant information found."

    context = "\n".join(retrieved_data)
    print("🔹 FAISS Retrieved Data:", retrieved_data)

    print("🛠 Generating response with Gemini...")
    response = model.generate_content(f"Context:\n{context}\n\nQuestion: {query}")

    if response and hasattr(response, "text"):
        return response.text.strip()
    else:
        return "LLM failed to generate an answer."
