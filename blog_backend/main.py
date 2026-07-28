from fastapi import FastAPI  # importer la classe FastAPI pour creer l'application

from app.config.database import Base, engine  # importer Base et engine pour pouvoir creer les tables dans la base de donnees
from app.models.user import User  # importer le modele User pour qu'il soit enregistre aupres de Base (sinon SQLAlchemy ne le connait pas et ne creera pas la table)
from app.routes.api import router  # importer le routeur qui contient toutes les routes de l'API

Base.metadata.create_all(bind=engine)  # creer toutes les tables definies dans Base (ici la table users) dans la base de donnees

app = FastAPI()  # creer l'instance de l'application FastAPI

app.include_router(router)  # brancher le routeur pour que toutes les routes definies soient actives

