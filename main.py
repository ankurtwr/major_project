from fastapi import FastAPI
from . import models
from .database import engine
from .routes import ask, auth

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(ask.router)
app.include_router(auth.router)