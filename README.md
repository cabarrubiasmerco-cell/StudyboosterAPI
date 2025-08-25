# StudyboosterAPI
# Simple Info API (SIA)

This is a simple **FastAPI-based project** that provides:
- ✅ Random **tips** (with optional topic filtering)
- ✅ Random **quotes**
- ✅ Ability for users to **submit feedback**

It’s lightweight, easy to run, and great for learning FastAPI basics.
---

## Features
- `GET /tips/random` → Returns a random tip (optionally filtered by topic).
- `GET /quotes/random` → Returns a random motivational quote.
- `POST /feedback` → Accepts user feedback and stores it in a JSON file.

---
Random Tips
  Get a random tip from different topics (e.g., health, study, productivity).
  Optional query parameter (?topic=...) lets you filter tips by category.
  
Random Quotes
  Returns a random motivational or inspirational quote.

Feedback Submission
  Accepts user feedback (feature + comment).
  Stores feedback persistently in feedback.json.
  Returns the stored feedback with a unique ID.

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/sia.git
   cd sia

   python -m venv venv
   
# Activate
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On Linux/Mac

## Create and activate a virtual environment
  pip install -r requirements.txt

## Install dependencies
  pip install -r requirements.txt

## Run the server
  python -m uvicorn app.main:app --reload

Example endpoints:
1. Get Random Tip
Request
  In bash terminal: GET /tips/random?topic=health
Response (json)
  {
  "id": 1,
  "topic": "health",
  "text": "Drink 8 glasses of water daily"
}

2. Get Random Quote
Request
  In bash terminal: GET /quotes/random
Response (json)
  {
  "id": 1,
  "text": "The best way to get started is to quit talking and begin doing.",
  "author": "Walt Disney"
}

3. Submit Feedback
Request (In bash terminal)
  POST /feedback
  Content-Type: application/json
  
  {
    "feature": "UI",
    "comment": "The design is clean and easy to use!"
  }
Response (json)
  {
  "id": 1,
  "feature": "UI",
  "comment": "The design is clean and easy to use!"
}


 
