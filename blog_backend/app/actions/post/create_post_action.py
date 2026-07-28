from sqlalchemy.orm import joinedload

from app.config.database import SessionLocal
from app.models.post import Post
from app.models.user import User
from app.requests.post.create_post_request import CreatePostRequest


def create_post_action(data: CreatePostRequest, author: User):
    db = SessionLocal()
    try:
        post = Post(
            title=data.title,
            content=data.content,
            author_id=author.id,
        )
        db.add(post)
        db.commit()
        db.refresh(post)
        post = (
            db.query(Post)
            .options(joinedload(Post.author), joinedload(Post.likes))
            .filter(Post.id == post.id)
            .first()
        )
        return post
    finally:
        db.close()
