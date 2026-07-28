from sqlalchemy.orm import joinedload

from app.config.database import SessionLocal
from app.models.post import Post


def get_post_action(post_id: int):
    db = SessionLocal()
    try:
        post = (
            db.query(Post)
            .options(joinedload(Post.author), joinedload(Post.likes))
            .filter(Post.id == post_id)
            .first()
        )
        return post
    finally:
        db.close()
