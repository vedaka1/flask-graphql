from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.domain.users.entities import User
from src.infrastructure.db.database import db


class UserModel(db.Model):  # type: ignore
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str | None] = mapped_column(nullable=True)
    last_name: Mapped[str | None] = mapped_column(nullable=True)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)

    def __repr__(self) -> str:
        return f"UserModel({self.__dict__})"


def map_to_user(entity: UserModel) -> User:
    return User(
        id=entity.id,
        email=entity.email,
        hashed_password=entity.hashed_password,
        first_name=entity.first_name,
        last_name=entity.last_name,
        is_verified=entity.is_verified,
    )
