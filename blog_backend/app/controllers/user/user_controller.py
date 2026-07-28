from app.actions.user.create_user_action import create_user_action
from app.actions.user.delete_user_action import delete_user_action
from app.actions.user.get_user_action import get_user_action
from app.actions.user.google_login_action import google_login_action
from app.actions.user.list_users_action import list_users_action
from app.actions.user.login_action import login_action
from app.actions.user.update_user_action import update_user_action
from app.requests.user.create_user_request import CreateUserRequest
from app.requests.user.google_login_request import GoogleLoginRequest
from app.requests.user.login_request import LoginRequest
from app.requests.user.update_user_request import UpdateUserRequest
from app.resources.user.user_resource import UserResource
from fastapi import HTTPException


def create_user_controller(data: CreateUserRequest):
    user = create_user_action(data)
    return UserResource.model_validate(user)


def list_users_controller():
    users = list_users_action()
    return [UserResource.model_validate(u) for u in users]


def get_user_controller(user_id: int):
    user = get_user_action(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return UserResource.model_validate(user)


def update_user_controller(user_id: int, data: UpdateUserRequest):
    user = update_user_action(user_id, data)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return UserResource.model_validate(user)


def delete_user_controller(user_id: int):
    deleted = delete_user_action(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")


def login_controller(data: LoginRequest):
    return login_action(data)


def google_login_controller(data: GoogleLoginRequest):
    return google_login_action(data)
