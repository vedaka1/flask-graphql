import logging
from uuid import UUID

from flask_sqlalchemy import SQLAlchemy

from src.domain.users.entities import User
from src.domain.users.repositories import UserRepositoryInterface
from src.infrastructure.db.models.user import UserModel, map_to_user

logger = logging.getLogger('__main__')


class UserRepository(UserRepositoryInterface):
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create(self, user: User) -> None:
        user_model = UserModel(
            id=user.id,
            email=user.email,
            hashed_password=user.hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
            is_verified=user.is_verified,
        )

        self.db.session.add(user_model)

        return None

    def get_many(self) -> list[User]:
        users = self.db.session.query(UserModel).all()

        return [map_to_user(user) for user in users]

    def get_by_id(self, id: UUID) -> User | None:
        user = self.db.session.get_one(UserModel, id)

        return map_to_user(user) if user else None

    def delete(self, id: UUID) -> None:
        user = self.db.session.get_one(UserModel, id)

        self.db.session.delete(user)
