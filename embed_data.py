import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle

# Paths
DATA_PATH = r"C:\Users\sri tejasw\buyogo\data\cleaned_hotel_bookings.csv"
FAISS_INDEX_PATH = r"C:\Users\sri tejasw\buyogo\embeddings\faiss_index.bin"
EMBEDDINGS_METADATA_PATH = r"C:\Users\sri tejasw\buyogo\embeddings\metadata.pkl"

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")  # Small & fast model for embeddings

def load_data(file_path):
    """Load cleaned booking data."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    return pd.read_csv(file_path)

def generate_embeddings(data):
    """Convert booking records to numerical embeddings."""
    records = data.apply(lambda row: f"Booking at {row['hotel']} by {row['country']} on {row['reservation_status_date']}. Status: {row['reservation_status']}", axis=1)
    embeddings = model.encode(records.tolist())  # Convert text to embeddings
    return np.array(embeddings, dtype="float32"), records.tolist()

def save_faiss_index(embeddings, records):
    """Save FAISS index & metadata for retrieval."""
    index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance index
    index.add(embeddings)  # Store embeddings in FAISS
    faiss.write_index(index, FAISS_INDEX_PATH)  # Save index

    with open(EMBEDDINGS_METADATA_PATH, "wb") as f:
        pickle.dump(records, f)  # Save original text data
    print(f"✅ FAISS index saved to {FAISS_INDEX_PATH}")

if __name__ == "__main__":
    print("🔄 Loading cleaned dataset...")
    df = load_data(DATA_PATH)

    if df is not None:
        print("✨ Generating embeddings...")
        embeddings, records = generate_embeddings(df)
        save_faiss_index(embeddings, records)
        print("🎉 Embedding process complete!")
