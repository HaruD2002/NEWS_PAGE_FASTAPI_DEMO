import jwt
from jose import jwt
import os

ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE = 30
JWT_REFRESH_TOKEN_EXPIRE = 60 * 24 * 7
secret_key = os.environ["JWT_SECRET_KEY"]
refresh_secret_key = os.environ["JWT_REFESH_SECRET_KEY"]

