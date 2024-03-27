from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateItinerary(BaseModel):
    date: datetime
    location: str
    plan_id: int
    
class UpdateItinerary(BaseModel):
    date: Optional[datetime]
    location: Optional[str]
