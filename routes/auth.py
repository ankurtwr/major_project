from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schema
import hashing
from database import engine, SessionLocal






app = FastAPI()
models.Base.metadata.create_all(engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
    

@app.post('/register',response_model=schema.Show_user,tags=['user'])
def register_user(request:schema.Register,db:Session = Depends(get_db)):
    new_user = models.User_Base(
        name = request.name,
        email = request.email,
        phone = request.phone,
        role = request.role,
        password = hashing.password_hash.hash(request.password)
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    