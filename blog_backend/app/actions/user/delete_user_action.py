from app.config.database import SessionLocal
from app.models.user import User


def delete_user_action(user_id: int) -> bool:
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return False

        db.delete(user)
        db.commit()
        return True
    finally:
        db.close()
