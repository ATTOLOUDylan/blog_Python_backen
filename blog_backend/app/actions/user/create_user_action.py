# Importation de la session de base de données
from app.config.database import SessionLocal
# Importation du modèle User (la table utilisateur en BDD)
from app.models.user import User
# Importation du schéma de validation pour la création d'un utilisateur
from app.requests.user.create_user_request import CreateUserRequest
from app.services.auth_service import hash_password


# Action qui gère la création d'un nouvel utilisateur en base de données
def create_user_action(data: CreateUserRequest):
    # Ouvre une connexion à la base de données
    db = SessionLocal()
    try:
        # Hash le mot de passe reçu avant de le stocker en base
        hashed_password = hash_password(data.password)
        # Crée une instance du modèle User avec les données reçues
        user = User(
            name=data.name,
            email=data.email,
            password=hashed_password,
        )
        # Ajoute le nouvel utilisateur à la session
        db.add(user)
        # Enregistre les modifications en base de données
        db.commit()
        # Rafraîchit l'objet pour récupérer l'id généré automatiquement
        db.refresh(user)
        # Retourne l'utilisateur créé
        return user
    finally:
        # Ferme la connexion à la base de données, même en cas d'erreur
        db.close()
