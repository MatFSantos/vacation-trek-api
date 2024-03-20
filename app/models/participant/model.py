from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Annotated

class CreateParticipant(BaseModel):
    name: Annotated[str, Field(max_length=200)]
    plan_id: int
    
class UpdateParticipant(BaseModel):
    name: Optional[Annotated[str, Field(max_length=200)]]
