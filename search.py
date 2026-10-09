from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post('/search')
def ask(query:str):
    return query
    