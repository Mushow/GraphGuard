from sqlalchemy.orm import sessionmaker
from database import engine, Base
from models import User
import hashlib

Session = sessionmaker(bind=engine)
session = Session()


def add_users():
    users = [
        User(username="user1", email="user1@example.com", full_name="User One",
             password=hashlib.sha256("password1".encode()).hexdigest()),
        User(username="user2", email="user2@example.com", full_name="User Two",
             password=hashlib.sha256("password2".encode()).hexdigest()),
    ]
    session.add_all(users)
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    add_users()
    print("Utilisateurs ajoutés avec succès")
