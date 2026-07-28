from app.config.database import SessionLocal
from app.models.user import User
from app.requests.user.update_user_request import UpdateUserRequest
from app.services.auth_service import hash_password


def update_user_action(user_id: int, data: UpdateUserRequest):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return None

        if data.name is not None:
            user.name = data.name
        if data.email is not None:
            user.email = data.email
        if data.password is not None:
            user.password = hash_password(data.password)

        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()
