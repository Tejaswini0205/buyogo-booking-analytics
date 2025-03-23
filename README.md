**Project Overview**
This project is a hotel booking analytics and question-answering system poweredby LLM (Large Language Model) with RAG. It processes hotel booking data, extracts insights, and provides a FastAPI-based REST API for analytics and natural language queries.

**Features**
✅ Data Processing – Cleans and structures hotel booking data
✅ Analytics & Insights – Generates revenue trends, cancellation rates, booking lead time, and geographical distribution
✅ Question-Answering (QA) – Uses FAISS-based RAG for answering booking-related questions
✅ REST API – Provides endpoints for analytics and QA
✅ Visualization – Generates insightful graphs & reports

**Installation & Setup**
1️⃣ Clone the repository
git clone https://github.com/Tejaswini0205/buyogo-booking-analytics
cd buyogo
2️⃣ Set up a virtual environment
Set up a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set up environment variables
Create a .env file and add:
GOOGLE_API_KEY=your_google_gemini_api_key
5️⃣ Run the FastAPI server
uvicorn backend.api.main:app --reload
The API will be available at http://127.0.0.1:8000/docs

**API Endpoints**
📌 POST /analytics – Returns booking insights
📌 POST /ask – Answers user questions about bookings
**Description**
This endpoint allows users to ask questions related to hotel booking data. It utilizes a Retrieval-Augmented Generation (RAG) system to provide insightful responses based on historical booking data, trends, and analytics.
Example Request to /ask
{
  "query": "Which locations had the highest cancellations?"
}
Example Response body
{
  "answers": "Mountain Lodge had the highest number of cancellations with three."
}
**Description**
This endpoint provides analytical insights based on hotel booking data. Users can request different metrics like revenue trends, booking distributions, and geographical statistics.
Example Request to /analytics
Geographical Distribution of Bookings:
{
  "metric": "geographical_distribution"
}
{
  "metric": "geographical_distribution",
  "result": {
    "PRT": 27000,
    "GBR": 10500,
    "FRA": 9000,
    "ESP": 7200,
    "DEU": 5400,
    "ITA": 3200,
    "IRL": 3100,
    "BEL": 2200,
    "BRA": 2100,
    "NLD": 2000
  }
}
 Booking Lead Time Distribution:
 {
  "metric": "lead_time_distribution"
}
{
  "metric": "lead_time_distribution",
  "result": {
    "0-10 days": 32000,
    "11-30 days": 15000,
    "31-60 days": 10000,
    "61-90 days": 7500,
    "91-120 days": 5000,
    "121-180 days": 4500,
    "181-365 days": 3000,
    "366+ days": 500
  }
}
Revenue Trends Over Time:
{
  "metric": "revenue_trends"
}
{
  "metric": "revenue_trends",
  "result": {
    "2015": {
      "January": 100000,
      "February": 120000,
      "March": 150000,
      "April": 170000,
      "May": 200000,
      "June": 250000,
      "July": 270000,
      "August": 300000,
      "September": 230000,
      "October": 200000,
      "November": 120000,
      "December": 150000
    },
    "2016": {
      "January": 200000,
      "February": 220000,
      "March": 250000,
      "April": 300000,
      "May": 350000,
      "June": 400000,
      "July": 500000,
      "August": 650000,
      "September": 450000,
      "October": 400000,
      "November": 350000,
      "December": 280000
    },
    "2017": {
      "January": 300000,
      "February": 320000,
      "March": 350000,
      "April": 400000,
      "May": 500000,
      "June": 600000,
      "July": 700000,
      "August": 750000,
      "September": 650000,
      "October": 600000,
      "November": 550000,
      "December": 500000
    }
  }
}
📊 Analytics Visualizations
The project includes various data visualizations that provide insights into hotel bookings:
->Top 10 Countries by Number of Bookings - (geographical_distribution.png)
->Booking Lead Time Distribution - (lead_time_distribution.png)
->Revenue Trends Over Time - (revenue_trends.png)
->These images are uploaded directly in the repository. You can find them by looking for the respective filenames.

