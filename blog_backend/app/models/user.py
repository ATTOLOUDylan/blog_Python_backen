from sqlalchemy import Column, Integer, String  # importer les types de colonnes pour definir le schema de la table

from app.config.database import Base  # importer la classe Base depuis la config pour creer le modele


class User(Base):  # declarer le modele User qui herite de Base
    __tablename__ = "users"  # nom de la table dans la base de donnees

    id = Column(Integer, primary_key=True, index=True)  # colonne id, cle primaire, indexee pour les recherches rapides
    name = Column(String)  # colonne name pour le nom de l'utilisateur
    email = Column(String, unique=True)  # colonne email, unique pour eviter les doublons
    password = Column(String)  # colonne password pour le mot de passe
