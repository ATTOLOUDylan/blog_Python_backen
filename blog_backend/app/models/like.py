from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from app.config.database import Base


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))

    __table_args__ = (UniqueConstraint("user_id", "post_id", name="unique_user_post_like"),)

    user = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")
