from fastapi import HTTPException

from app.actions.like.toggle_like_action import toggle_like_action
from app.models.user import User


def toggle_like_controller(post_id: int, current_user: User):
    result = toggle_like_action(post_id, current_user)
    if not result["found"]:
        raise HTTPException(status_code=404, detail="Post introuvable")
    return {"liked": result["liked"]}
