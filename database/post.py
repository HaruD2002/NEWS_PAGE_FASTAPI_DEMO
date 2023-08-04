from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from .user import User
import util.enum as enum


class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey(User.id))
    post_title = Column(String(100))
    post = Column(String(8000))
    created_dt = Column(DateTime, default=enum.NOW)
    author = relationship('User', back_populates='posts')
    post_comment = relationship('Comment', back_populates='posts')