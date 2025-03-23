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
Example Request to /ask
{
  "query": "What is the most booked hotel?"
}
Example Request to /analytics
{
  "metric": "revenue_trends"
}
