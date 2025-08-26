
from fastapi import APIRouter

router = APIRouter()

@router.get("/events")
def get_events():
    return [
        {"id": 1, "title": "Math Review Session", "date": "2025-09-01", "location": "Room 201"},
        {"id": 2, "title": "Physics Quiz", "date": "2025-09-05", "location": "Online"}
    ]
