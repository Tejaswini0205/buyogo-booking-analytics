import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer

# Ensure the embeddings directory exists
os.makedirs("embeddings", exist_ok=True)

# Sample dataset (Replace with your actual booking dataset)
data = [
    {"text": "Booking at City Hotel on 2015-09-16. Status: Canceled. Reason: No show"},
    {"text": "Booking at Beach Resort on 2016-02-10. Status: Canceled. Reason: Payment failed"},
    {"text": "Booking at Mountain Lodge on 2016-07-20. Status: Canceled. Reason: Customer changed plans"},
]

# Load embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Generate embeddings
texts = [item["text"] for item in data]
embeddings = model.encode(texts)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index and metadata
faiss.write_index(index, "embeddings/faiss_index.bin")
with open("embeddings/metadata.pkl", "wb") as f:
    pickle.dump(texts, f)

print("✅ FAISS index created and saved successfully!")
