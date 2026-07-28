from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String, nullable=True)
    google_id = Column(String, nullable=True, unique=True)
    is_admin = Column(Boolean, default=False)

    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    likes = relationship("Like", back_populates="user")
