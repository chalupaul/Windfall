from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class User(declarative_base()):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
