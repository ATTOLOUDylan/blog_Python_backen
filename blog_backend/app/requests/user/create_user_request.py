# Importation de BaseModel pour créer un modèle de données et EmailStr pour valider les emails
from pydantic import BaseModel, EmailStr


# Schéma de validation pour la création d'un utilisateur
# BaseModel vérifie automatiquement les types et valide le format de l'email
class CreateUserRequest(BaseModel):
    name: str          # Nom de l'utilisateur
    email: EmailStr    # Email avec validation automatique du format
    password: str      # Mot de passe (à hasher plus tard)
