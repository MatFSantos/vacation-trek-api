from pydantic import BaseModel
from typing import Optional
from datetime import date

class CreateItinerary(BaseModel):
    date: date
    location: str
    plan_id: int
    
class UpdateItinerary(BaseModel):
    date: Optional[date]
    location: Optional[str]
