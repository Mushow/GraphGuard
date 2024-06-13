from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    import models
    print("Initialisation de la base de données...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables créées avec succès.")
    except exc.SQLAlchemyError as e:
        print("Erreur lors de la création des tables :", e)
