import os

from fastapi import HTTPException
from google.auth.transport import requests
from google.oauth2 import id_token

from app.config.database import SessionLocal
from app.models.user import User
from app.requests.user.google_login_request import GoogleLoginRequest
from app.services.auth_service import create_access_token

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


def google_login_action(data: GoogleLoginRequest) -> dict:
    try:
        idinfo = id_token.verify_oauth2_token(data.token, requests.Request(), GOOGLE_CLIENT_ID)
    except ValueError:
        raise HTTPException(status_code=401, detail="Token Google invalide")

    email = idinfo["email"]
    name = idinfo.get("name", email)
    google_id = idinfo["sub"]

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            user = User(name=name, email=email, google_id=google_id, password=None)
            db.add(user)
            db.commit()
            db.refresh(user)
        elif user.google_id is None:
            user.google_id = google_id
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": user.email})
        return {"access_token": token, "token_type": "bearer"}
    finally:
        db.close()
