from fastapi import APIRouter, Depends
from models.user import UserCreate
from sqlalchemy.orm import Session
from database.database import get_db
from database.operations import user as user_db
route = APIRouter()


@route.post('/user/register')
async def register(user: UserCreate, db:Session = Depends(get_db)):
    return user_db.createUser(db, user)
