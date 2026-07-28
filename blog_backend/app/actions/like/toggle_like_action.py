from app.config.database import SessionLocal
from app.models.like import Like
from app.models.post import Post
from app.models.user import User


def toggle_like_action(post_id: int, user: User) -> dict:
    db = SessionLocal()
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if post is None:
            return {"found": False, "liked": False}

        existing_like = (
            db.query(Like)
            .filter(Like.user_id == user.id, Like.post_id == post_id)
            .first()
        )

        if existing_like:
            db.delete(existing_like)
            db.commit()
            return {"found": True, "liked": False}

        like = Like(user_id=user.id, post_id=post_id)
        db.add(like)
        db.commit()
        return {"found": True, "liked": True}
    finally:
        db.close()
