from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.database import Base
from db.database import engine
from db import models
from routers import user, post, comment
from auth import authentication



app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)


app.mount('/files',  StaticFiles(directory='uploaded files'), name='files')



Base.metadata.create_all(engine)


@app.get('/')
def home():
    return 'First Page'