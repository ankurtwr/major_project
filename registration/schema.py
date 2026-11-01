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
    