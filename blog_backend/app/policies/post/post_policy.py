from fastapi import HTTPException

from app.models.post import Post
from app.models.user import User


def authorize_modify_post(user: User, post: Post) -> None:
    if post.author_id != user.id and not user.is_admin:
        raise HTTPException(status_code=403, detail="Non autorise a modifier ce post")
