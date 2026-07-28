from fastapi import HTTPException

from app.actions.comment.create_comment_action import create_comment_action
from app.actions.comment.delete_comment_action import delete_comment_action
from app.actions.comment.list_comments_action import list_comments_action
from app.models.user import User
from app.requests.comment.create_comment_request import CreateCommentRequest
from app.resources.comment.comment_resource import CommentResource


def create_comment_controller(post_id: int, data: CreateCommentRequest, current_user: User):
    comment = create_comment_action(post_id, data, current_user)
    if comment is None:
        raise HTTPException(status_code=404, detail="Post introuvable")
    return CommentResource.from_comment(comment)


def list_comments_controller(post_id: int):
    comments = list_comments_action(post_id)
    return [CommentResource.from_comment(c) for c in comments]


def delete_comment_controller(comment_id: int, current_user: User):
    deleted = delete_comment_action(comment_id, current_user)
    if not deleted:
        raise HTTPException(status_code=404, detail="Commentaire introuvable")
