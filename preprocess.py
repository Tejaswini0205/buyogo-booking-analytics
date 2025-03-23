import pandas as pd
import numpy as np
import os

# Define input and output file paths
DATA_PATH = r"C:\Users\sri tejasw\buyogo\data\hotel_bookings.csv"
OUTPUT_PATH = r"C:\Users\sri tejasw\buyogo\data\cleaned_hotel_bookings.csv"

def load_data(file_path):
    """Loads the dataset into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    return pd.read_csv(file_path)

def clean_data(df):
    """Cleans and preprocesses the dataset."""
    # Drop irrelevant columns (if they exist)
    cols_to_drop = ["agent", "company"]
    existing_cols = [col for col in cols_to_drop if col in df.columns]
    df.drop(columns=existing_cols, inplace=True)

    print(f"Dropped columns: {existing_cols}")

    # Handle missing values
    df.fillna({
        "children": 0,  
        "country": "Unknown",  
    }, inplace=True)

    # Convert date columns to datetime format
    df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"])

    # Ensure adr (Average Daily Rate) is non-negative
    df = df[df["adr"] >= 0]

    # Convert categorical columns to proper type
    categorical_cols = ["hotel", "meal", "market_segment", "distribution_channel", "customer_type"]
    for col in categorical_cols:
        df[col] = df[col].astype("category")

    return df

def save_cleaned_data(df, output_path):
    """Saves the cleaned dataset."""
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    print("🔄 Loading dataset...")
    df = load_data(DATA_PATH)
    
    if df is not None:
        print("✨ Cleaning data...")
        df = clean_data(df)
        save_cleaned_data(df, OUTPUT_PATH)
        print("🎉 Preprocessing complete!")
