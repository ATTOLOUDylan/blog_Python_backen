# Importation de BaseModel pour créer un modèle de données
from pydantic import BaseModel


# Resource qui filtre les données renvoyées au frontend
# On expose uniquement les champs nécessaires, jamais le mot de passe
class UserResource(BaseModel):
    id: int      # Identifiant unique de l'utilisateur
    name: str    # Nom de l'utilisateur
    email: str   # Email de l'utilisateur

    # Configuration qui permet à Pydantic de lire directement un objet SQLAlchemy
    class Config:
        from_attributes = True
