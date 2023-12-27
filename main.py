from fastapi import FastAPI
from db.database import Base
from db.database import engine
from db import models



app = FastAPI()

Base.metadata.create_all(engine)


@app.get('/')
def home():
    return 'First Page'