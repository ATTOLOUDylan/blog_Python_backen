# Importation de la session de base de donnees
from app.config.database import SessionLocal
# Importation du modele User (la table utilisateur en BDD)
from app.models.user import User


# Action qui recupere tous les utilisateurs depuis la base de donnees
def list_users_action():
    # Ouvre une connexion a la base de donnees
    db = SessionLocal()
    try:
        # Recupere tous les utilisateurs
        users = db.query(User).all()
        # Retourne la liste des utilisateurs
        return users
    finally:
        # Ferme la connexion a la base de donnees, meme en cas d'erreur
        db.close()
