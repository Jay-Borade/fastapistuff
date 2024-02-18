from .database import BASE
from sqlalchemy import Column, Integer, String

class Blog(BASE):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    
    