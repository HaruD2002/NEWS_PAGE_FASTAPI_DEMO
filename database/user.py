from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    last_name = Column(String(55))
    first_name = Column(String(55))
    email = Column(String(155))
    phone_no = Column(String(11))
    posts = relationship('Post', back_populates='author')
    comments = relationship('Comment', back_populates='comment_author')