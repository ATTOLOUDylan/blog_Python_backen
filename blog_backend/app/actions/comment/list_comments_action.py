from sqlalchemy.orm import joinedload

from app.config.database import SessionLocal
from app.models.comment import Comment


def list_comments_action(post_id: int):
    db = SessionLocal()
    try:
        comments = (
            db.query(Comment)
            .options(joinedload(Comment.author))
            .filter(Comment.post_id == post_id)
            .all()
        )
        return comments
    finally:
        db.close()
