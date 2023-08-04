from fastapi import APIRouter
from fastapi_jwt_auth import AuthJWT
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


route = APIRouter()



@route.get('/user')
def user():
    return "Duy"