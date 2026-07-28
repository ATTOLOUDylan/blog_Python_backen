# Importation de l'action qui contient la logique métier de création d'utilisateur
from app.actions.user.create_user_action import create_user_action
# Importation des nouvelles actions pour lister et recuperer un utilisateur
from app.actions.user.list_users_action import list_users_action
from app.actions.user.get_user_action import get_user_action
# Importation du schéma de validation pour la création d'un utilisateur
from app.requests.user.create_user_request import CreateUserRequest
# Importation de la resource qui filtre les données à renvoyer
from app.resources.user.user_resource import UserResource
# Importation de HTTPException pour lever des erreurs HTTP (ex: 404)
from fastapi import HTTPException


# Controller qui orchestre la création d'un utilisateur
# Il ne contient aucune logique métier, il délègue tout à l'Action
def create_user_controller(data: CreateUserRequest):
    # Appelle l'action qui gère la création en base de données
    user = create_user_action(data)
    # Convertit l'objet SQLAlchemy en Resource filtrée (sans le mot de passe)
    return UserResource.model_validate(user)


# Controller qui recupere la liste de tous les utilisateurs
def list_users_controller():
    # Appelle l'action qui recupere tous les utilisateurs
    users = list_users_action()
    # Transforme chaque utilisateur en Resource (sans le mot de passe)
    return [UserResource.model_validate(u) for u in users]


# Controller qui recupere un utilisateur specifique par son id
def get_user_controller(user_id: int):
    # Appelle l'action qui recupere l'utilisateur par id
    user = get_user_action(user_id)
    # Si l'utilisateur n'existe pas, leve une erreur HTTP 404
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    # Convertit l'objet SQLAlchemy en Resource filtrée (sans le mot de passe)
    return UserResource.model_validate(user)
