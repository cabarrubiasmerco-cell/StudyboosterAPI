from fastapi import FastAPI, HTTPException
from typing import Optional, List
from random import choice
import json, os

from .schemas import Tip, Quote, FeedbackIn, FeedbackOut
from .data import TIPS, QUOTES
from events import routes as events_routes


app = FastAPI(
    title="Study Booster API",
    description="Simple API that returns study tips & motivational quotes.",
    version="1.0.0"
)

app.include_router(events_routes.router, prefix="/events", tags=["Events"])


app.include_router(events_routes.router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", tags=["info"])
def root():
    return {
        "name": "Study Booster API",
        "endpoints": ["/tips", "/tips/random", "/quotes/random", "/feedback"],
        "docs": "/docs"
    }

@app.get("/tips", response_model=List[Tip], tags=["tips"])
def get_tips(topic: Optional[str] = None):
    items = [t for t in TIPS if topic is None or t["topic"].lower() == topic.lower()]
    if not items:
        raise HTTPException(status_code=404, detail="No tips found for that topic.")
    return items

@app.get("/tips/random", response_model=Tip, tags=["tips"])
def random_tip(topic: Optional[str] = None):
    items = [t for t in TIPS if topic is None or t["topic"].lower() == topic.lower()]
    if not items:
        raise HTTPException(status_code=404, detail="No tips found for that topic.")
    return choice(items)

@app.get("/quotes/random", response_model=Quote, tags=["quotes"])
def random_quote():
    return choice(QUOTES)

FEEDBACK_DB = "feedback.json"

@app.post("/feedback", response_model=FeedbackOut, status_code=201, tags=["feedback"])
def create_feedback(payload: FeedbackIn):
    data = []
    if os.path.exists(FEEDBACK_DB):
        with open(FEEDBACK_DB, "r", encoding="utf-8") as f:
            data = json.load(f)
    new_row = {"id": len(data) + 1, **payload.dict()}
    data.append(new_row)
    with open(FEEDBACK_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return new_row
