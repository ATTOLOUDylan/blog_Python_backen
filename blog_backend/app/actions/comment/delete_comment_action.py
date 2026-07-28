from app.config.database import SessionLocal
from app.models.comment import Comment
from app.models.user import User
from app.policies.comment.comment_policy import authorize_delete_comment


def delete_comment_action(comment_id: int, current_user: User) -> bool:
    db = SessionLocal()
    try:
        comment = db.query(Comment).filter(Comment.id == comment_id).first()
        if comment is None:
            return False

        authorize_delete_comment(current_user, comment)

        db.delete(comment)
        db.commit()
        return True
    finally:
        db.close()
