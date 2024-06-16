import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User as UserModel
from database import SessionLocal


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        # Expose only the id and username fields to avoid exposing sensitive data
        only_fields = ('id', 'username')


class Query(graphene.ObjectType):
    all_users = graphene.List(User)

    def resolve_all_users(self, info):
        session = SessionLocal()
        return session.query(UserModel).all()


schema = graphene.Schema(query=Query)
