from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Annotated
from datetime import date

class CreatePlan(BaseModel):
    title: Annotated[str,Field(max_length=100)]
    description: Annotated[str,Field(max_length=300)]
    date_start: date
    date_end: date
    user_id: int

class UpdatePlan(BaseModel):
    title: Optional[Annotated[str,Field(max_length=100)]]
    description: Optional[Annotated[str,Field(max_length=300)]]
    date_start: Optional[date]
    date_end: Optional[date]