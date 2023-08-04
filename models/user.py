from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    name: str
    DoB: str
    phoneNo: Optional[str] = None # optional field can be provide or empty must declear a type in []
    
