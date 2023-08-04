from fastapi import APIRouter


route = APIRouter()

@route.get('/post')
def get_post():
    return 'duy post'