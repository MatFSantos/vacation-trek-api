from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Annotated

class CreateUser(BaseModel):
    name: Annotated[str, Field(max_length=200)]
    email: Annotated[str, Field(max_length=100)]
    password: Annotated[str, Field(max_length=200)]
    
class UpdateUser(BaseModel):
    name: Optional[Annotated[str, Field(max_length=200)]]
    email: Optional[Annotated[str, Field(max_length=100)]]
    password: Optional[Annotated[str, Field(max_length=200)]]

class LoginUser(BaseModel):
    email: Annotated[str, Field(max_length=100)]
    password: Annotated[str, Field(max_length=200)]

class VerifyUser(BaseModel):
    email: Annotated[str, Field(max_length=100)]