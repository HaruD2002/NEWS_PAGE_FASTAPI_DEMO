from typing import Optional, Union
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    pass

class UserModel(BaseModel):
    last_name: str
    first_name: str
    email: str
    phone_no: str

class UserCreate(UserModel):
    password: str
    
    class Config:
        orm_mode = True
