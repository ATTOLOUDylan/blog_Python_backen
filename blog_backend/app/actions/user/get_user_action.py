# Importation de la session de base de donnees
from app.config.database import SessionLocal
# Importation du modele User (la table utilisateur en BDD)
from app.models.user import User


# Action qui recupere un utilisateur specifique par son id
def get_user_action(user_id: int):
    # Ouvre une connexion a la base de donnees
    db = SessionLocal()
    try:
        # Recupere l'utilisateur correspondant a l'id fourni
        user = db.query(User).filter(User.id == user_id).first()
        # Retourne l'utilisateur (ou None si introuvable)
        return user
    finally:
        # Ferme la connexion a la base de donnees, meme en cas d'erreur
        db.close()
