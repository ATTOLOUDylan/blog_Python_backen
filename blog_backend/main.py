from fastapi import FastAPI

from app.config.database import Base, engine
from app.models.comment import Comment
from app.models.like import Like
from app.models.post import Post
from app.models.user import User
from app.routes.api import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
