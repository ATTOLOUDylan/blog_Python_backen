from fastapi import HTTPException

from app.models.comment import Comment
from app.models.user import User


def authorize_delete_comment(user: User, comment: Comment) -> None:
    if comment.author_id != user.id and not user.is_admin:
        raise HTTPException(status_code=403, detail="Non autorise a supprimer ce commentaire")
