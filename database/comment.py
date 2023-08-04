from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from .user import User
from .post import Post

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey(User.id))
    post_id = Column(ForeignKey(Post.id))
    comment_string = Column(String(2000))
    comment_author = relationship('User', back_populates='comments')
    posts = relationship('Post', back_populates='post_comment')

