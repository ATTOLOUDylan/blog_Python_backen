import os  # importer le module os pour interagir avec le systeme (variables d'environnement, fichiers, etc.)

from dotenv import load_dotenv  # importer load_dotenv pour charger les variables du fichier .env
from sqlalchemy import create_engine  # importer create_engine pour creer le moteur de connexion a la base de donnees
from sqlalchemy.orm import declarative_base, sessionmaker  # importer declarative_base pour definir les modeles et sessionmaker pour creer les sessions de connexion

load_dotenv()  # charger automatiquement les variables du fichier .env dans l'environnement

DATABASE_URL = os.getenv("DATABASE_URL")  # recuperer la variable DATABASE_URL depuis le fichier .env

engine = create_engine(DATABASE_URL)  # creer le moteur de connexion a la base de donnees avec l'URL recuperee

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # creer une classe de session liee au moteur, sans commit ni flush automatiques

Base = declarative_base()  # creer la classe de base pour declarer tous les modeles SQLAlchemy
