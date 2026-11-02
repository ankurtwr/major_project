from database import Base
from sqlalchemy import Column, Integer, String

class User_Base(Base):
    __tablename__ = 'User_Base'
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(200))
    email = Column(String(250))
    phone = Column(String(250))
    password = Column(String(250))
    role = Column(String(200))
    