# Importation du routeur de FastAPI pour définir les routes
from fastapi import APIRouter
# Importation des controllers pour chaque endpoint
from app.controllers.user.user_controller import create_user_controller, list_users_controller, get_user_controller
# Importation du schéma de validation pour la création d'un utilisateur
from app.requests.user.create_user_request import CreateUserRequest

# Création de l'instance du routeur qui regroupera toutes les routes de l'API
router = APIRouter()


# Route POST /users — reçoit les données d'un nouvel utilisateur
# FastAPI valide automatiquement le body de la requête avec CreateUserRequest
@router.post("/users")
def create_user(data: CreateUserRequest):
    # Délègue la création au controller
    return create_user_controller(data)


# Route GET /users — retourne la liste de tous les utilisateurs
@router.get("/users")
def list_users():
    # Délègue la récupération de la liste au controller
    return list_users_controller()


# Route GET /users/{user_id} — retourne un utilisateur spécifique par son id
# FastAPI récupère automatiquement user_id depuis l'URL
@router.get("/users/{user_id}")
def get_user(user_id: int):
    # Délègue la récupération au controller
    return get_user_controller(user_id)
