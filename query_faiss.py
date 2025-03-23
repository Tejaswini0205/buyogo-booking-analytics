import faiss
import pickle
import re
from collections import Counter
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Paths to FAISS index and metadata
INDEX_PATH = "embeddings/faiss_index.bin"
METADATA_PATH = "embeddings/metadata.pkl"

# Load FAISS index
print("🔄 Loading FAISS index...")
index = faiss.read_index(INDEX_PATH)

# Load metadata (text data corresponding to embeddings)
with open(METADATA_PATH, "rb") as f:
    texts = pickle.load(f)

# Load sentence embedding model
print("🔄 Loading embedding model...")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load Generative AI Model for RAG
print("🧠 Loading AI model for answering questions...")
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def search_faiss(query, k=20):
    """Search FAISS index and return top-k relevant results."""
    query_embedding = model.encode([query])  
    _, indices = index.search(query_embedding, k)  
    return [texts[i] for i in indices[0] if i < len(texts)]  

def extract_hotel_names(data):
    """Extract hotel names from retrieved FAISS results."""
    hotel_pattern = re.compile(r"Booking at ([\w\s]+) on")  
    hotels = [match.group(1) for text in data if (match := hotel_pattern.search(text))]
    return hotels

def get_most_common_location(context):
    """Find the most frequently mentioned hotel/location."""
    hotel_list = extract_hotel_names(context)
    location_counts = Counter(hotel_list)
    most_common_location = location_counts.most_common(1)
    return most_common_location[0] if most_common_location else ("No location found", 0)

# Get user input for query
user_query = input("🔍 Enter your question: ")

# Search FAISS for relevant results
retrieved_context = search_faiss(user_query, k=50)

# Determine most frequent location
top_location, count = get_most_common_location(retrieved_context)

# Generate answer using RAG model if needed
if "location" in user_query.lower() or "hotel" in user_query.lower():
    generated_answer = f"{top_location} ({count} times mentioned)"
else:
    generated_answer = " ".join(retrieved_context[:5])

# Display output
print("\n🔎 FAISS Retrieved Context:", retrieved_context)
print(f"\n📍 Most Frequent Location: {generated_answer}")
