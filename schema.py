from pydantic import BaseModel

class Register(BaseModel):
    name : str
    email : str
    phone : str
    password : str
    role : str
    
class Show_user(BaseModel):
    name : str
    role : str

class Successful(BaseModel):
    msg : str
    
class login_credentials(BaseModel):
    id : int
    password : str
    