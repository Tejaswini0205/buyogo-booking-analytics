import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define data path
DATA_PATH = r"C:\Users\sri tejasw\buyogo\data\cleaned_hotel_bookings.csv"

def load_cleaned_data(file_path):
    """Loads the cleaned dataset into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        print(f"❌ Error: File not found at {file_path}")
        return None
    return pd.read_csv(file_path)

def revenue_trends(df):
    """Plots total revenue trends over time."""
    df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"], errors="coerce")

    # Correct revenue calculation
    df["total_revenue"] = df["adr"] * (df["stays_in_week_nights"] + df["stays_in_weekend_nights"])

    revenue = df.groupby(df["reservation_status_date"].dt.to_period("M"))["total_revenue"].sum()

    plt.figure(figsize=(10, 5))
    revenue.plot(kind="line", marker="o", color="b")
    plt.title("Revenue Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def cancellation_rate(df):
    """Returns the percentage of cancelled bookings."""
    return (df["is_canceled"].sum() / len(df)) * 100

def geographical_distribution(df):
    """Plots geographical distribution of bookings."""
    if "country" in df.columns:
        country_counts = df["country"].value_counts().head(10)  # Top 10 countries

        plt.figure(figsize=(10, 5))
        sns.barplot(x=country_counts.index, y=country_counts.values, palette="coolwarm")
        plt.title("Top 10 Countries by Bookings")
        plt.xlabel("Country")
        plt.ylabel("Number of Bookings")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("⚠️ Warning: 'country' column missing, skipping plot.")

def booking_lead_time(df):
    """Plots distribution of lead time (days before booking)."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df["lead_time"], bins=50, kde=True, color="purple")
    plt.title("Booking Lead Time Distribution")
    plt.xlabel("Lead Time (days)")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

def most_common_cancellation_reason(df):
    """Finds the most common reason for booking cancellations."""
    if "reservation_status" in df.columns:
        canceled_df = df[df["reservation_status"] == "Canceled"]
        if "cancellation_reason" in canceled_df.columns and not canceled_df["cancellation_reason"].empty:
            return canceled_df["cancellation_reason"].mode()[0]  # Most frequent reason
        else:
            return "Cancellation reasons not available in dataset"
    return "No cancellations found"

def get_analytics(query_type):
    """Handles analytics queries and returns relevant insights."""
    df = load_cleaned_data(DATA_PATH)
    if df is None:
        return {"error": "Data file not found"}

    if query_type == "popular_checkin_month":
        return df["arrival_date_month"].mode()[0]

    if query_type == "cancellation_rate":
        return f"{cancellation_rate(df):.2f}%"

    if query_type == "most_common_cancellation_reason":
        return most_common_cancellation_reason(df)

    if query_type == "revenue_trends":
        revenue_trends(df)
        return "Revenue trends graph generated."

    return {"error": "Unknown analytics query"}

if __name__ == "__main__":
    df = load_cleaned_data(DATA_PATH)

    if df is not None:
        print("📊 Generating analytics...")
        
        print(f"Total Revenue: {df['adr'].sum()}")  # Note: This is now fixed
        print(f"Cancellation Rate: {cancellation_rate(df):.2f}%")
        print(f"Most Common Cancellation Reason: {most_common_cancellation_reason(df)}")

        # Generate visualizations
        revenue_trends(df)
        geographical_distribution(df)
        booking_lead_time(df)

        print("✅ Analytics completed!")
