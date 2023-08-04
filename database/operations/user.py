from database.models.user import User
from sqlalchemy.orm import Session
from models.user import UserCreate
from models.auth.auth import get_hash_password

def createUser(db: Session, user:UserCreate):
    user.password = get_hash_password(user.password)
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user