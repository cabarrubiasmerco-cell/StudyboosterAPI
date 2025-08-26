from pydantic import BaseModel, Field

class Tip(BaseModel):
    id: int
    topic: str
    text: str

class Quote(BaseModel):
    id: int
    text: str
    author: str

class FeedbackIn(BaseModel):
    feature: str = Field(..., min_length=2)
    comment: str = Field(..., min_length=3)

class FeedbackOut(FeedbackIn):
    id: int
