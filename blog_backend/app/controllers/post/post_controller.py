from fastapi import HTTPException

from app.actions.post.create_post_action import create_post_action
from app.actions.post.delete_post_action import delete_post_action
from app.actions.post.get_post_action import get_post_action
from app.actions.post.list_posts_action import list_posts_action
from app.actions.post.update_post_action import update_post_action
from app.models.user import User
from app.requests.post.create_post_request import CreatePostRequest
from app.requests.post.update_post_request import UpdatePostRequest
from app.resources.post.post_resource import PostResource


def create_post_controller(data: CreatePostRequest, current_user: User):
    post = create_post_action(data, current_user)
    return PostResource.from_post(post)


def list_posts_controller(
    search: str | None = None,
    author_id: int | None = None,
    skip: int = 0,
    limit: int = 10,
):
    posts = list_posts_action(search=search, author_id=author_id, skip=skip, limit=limit)
    return [PostResource.from_post(p) for p in posts]


def get_post_controller(post_id: int):
    post = get_post_action(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post introuvable")
    return PostResource.from_post(post)


def update_post_controller(post_id: int, data: UpdatePostRequest, current_user: User):
    post = update_post_action(post_id, data, current_user)
    if post is None:
        raise HTTPException(status_code=404, detail="Post introuvable")
    return PostResource.from_post(post)


def delete_post_controller(post_id: int, current_user: User):
    deleted = delete_post_action(post_id, current_user)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post introuvable")
