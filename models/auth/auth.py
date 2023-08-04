import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

key = os.getenv("JWT_SECRET_KEY")
algorithm = os.getenv("JWT_ALGORITHM")
expire_time = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oath2_Schema = OAuth2PasswordBearer(tokenUrl="token")

def vertify_password(password,hashed_password):
    return pwd_context.verify(password, hashed_password)

def get_hash_password(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow + timedelta(minutes=expire_time)
    
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, key=key, algorithm=algorithm)
    return encode_jwt