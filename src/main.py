from fastapi import FastAPI
from routes import *
from database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    database.create_db()

app.include_router(home.route)
app.include_router(user.route)
app.include_router(post.route)
app.include_router(comment.route)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)