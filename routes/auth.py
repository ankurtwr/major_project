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

@app.post('/login',response_model = schema.Successful,tags=['user'])
def login(request:schema.login_credentials,response : Response,db: Session = Depends(get_db)):
    id = request.id
    password = request.password
    
    user = db.query(models.User_Base).filter(models.User_Base.id == id).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        msg = f"user with id = {id} is not registerd"
        return {'msg':msg}
    else:
        check = hashing.password_hash.verify(password,user.password)
        if check:
            response.status_code = status.HTTP_200_OK
            msg = 'login successful'
            return {'msg':msg}
        else:
            response.status_code = status.HTTP_401_UNAUTHORIZED
            msg = 'incorrect password'
            return {'msg':msg}
            
        
    