from app.config.database import SessionLocal
from app.models.post import Post
from app.models.user import User
from app.policies.post.post_policy import authorize_modify_post


def delete_post_action(post_id: int, current_user: User) -> bool:
    db = SessionLocal()
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if post is None:
            return False

        authorize_modify_post(current_user, post)

        db.delete(post)
        db.commit()
        return True
    finally:
        db.close()
