from fastapi import APIRouter


route = APIRouter()


@route.get('/')
async def main():
    return {
        'code': 200,
        'message': "api call"
}
