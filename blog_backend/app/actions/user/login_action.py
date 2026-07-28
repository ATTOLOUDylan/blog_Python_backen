from fastapi import HTTPException

from app.config.database import SessionLocal
from app.models.user import User
from app.requests.user.login_request import LoginRequest
from app.services.auth_service import create_access_token, verify_password


def login_action(data: LoginRequest) -> dict:
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == data.email).first()
        if user is None or user.password is None or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")

        token = create_access_token({"sub": user.email})
        return {"access_token": token, "token_type": "bearer"}
    finally:
        db.close()
