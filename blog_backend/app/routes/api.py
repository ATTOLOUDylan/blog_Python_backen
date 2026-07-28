from fastapi import APIRouter, Depends

from app.controllers.comment.comment_controller import (
    create_comment_controller,
    delete_comment_controller,
    list_comments_controller,
)
from app.controllers.like.like_controller import toggle_like_controller
from app.controllers.post.post_controller import (
    create_post_controller,
    delete_post_controller,
    get_post_controller,
    list_posts_controller,
    update_post_controller,
)
from app.controllers.user.user_controller import (
    create_user_controller,
    delete_user_controller,
    get_user_controller,
    google_login_controller,
    list_users_controller,
    login_controller,
    update_user_controller,
)
from app.middlewares.auth_middleware import get_current_user
from app.models.user import User
from app.requests.comment.create_comment_request import CreateCommentRequest
from app.requests.post.create_post_request import CreatePostRequest
from app.requests.post.update_post_request import UpdatePostRequest
from app.requests.user.create_user_request import CreateUserRequest
from app.requests.user.google_login_request import GoogleLoginRequest
from app.requests.user.login_request import LoginRequest
from app.requests.user.update_user_request import UpdateUserRequest

router = APIRouter()


# --- Users ---

@router.post("/users")
def create_user(data: CreateUserRequest):
    return create_user_controller(data)


@router.get("/users")
def list_users():
    return list_users_controller()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return get_user_controller(user_id)


@router.put("/users/{user_id}")
def update_user(user_id: int, data: UpdateUserRequest):
    return update_user_controller(user_id, data)


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return delete_user_controller(user_id)


# --- Auth ---

@router.post("/login")
def login(data: LoginRequest):
    return login_controller(data)


@router.post("/auth/google")
def google_login(data: GoogleLoginRequest):
    return google_login_controller(data)


# --- Posts ---

@router.post("/posts")
def create_post(data: CreatePostRequest, current_user: User = Depends(get_current_user)):
    return create_post_controller(data, current_user)


@router.get("/posts")
def list_posts(
    search: str | None = None,
    author_id: int | None = None,
    skip: int = 0,
    limit: int = 10,
):
    return list_posts_controller(search=search, author_id=author_id, skip=skip, limit=limit)


@router.get("/posts/{post_id}")
def get_post(post_id: int):
    return get_post_controller(post_id)


@router.put("/posts/{post_id}")
def update_post(
    post_id: int,
    data: UpdatePostRequest,
    current_user: User = Depends(get_current_user),
):
    return update_post_controller(post_id, data, current_user)


@router.delete("/posts/{post_id}")
def delete_post(post_id: int, current_user: User = Depends(get_current_user)):
    return delete_post_controller(post_id, current_user)


# --- Comments ---

@router.post("/posts/{post_id}/comments")
def create_comment(
    post_id: int,
    data: CreateCommentRequest,
    current_user: User = Depends(get_current_user),
):
    return create_comment_controller(post_id, data, current_user)


@router.get("/posts/{post_id}/comments")
def list_comments(post_id: int):
    return list_comments_controller(post_id)


@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, current_user: User = Depends(get_current_user)):
    return delete_comment_controller(comment_id, current_user)


# --- Likes ---

@router.post("/posts/{post_id}/like")
def toggle_like(post_id: int, current_user: User = Depends(get_current_user)):
    return toggle_like_controller(post_id, current_user)
