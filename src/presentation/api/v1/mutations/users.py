from typing import Any
from uuid import UUID

from ariadne import convert_kwargs_to_snake_case
from flask_sqlalchemy import SQLAlchemy
from graphql import GraphQLResolveInfo

from src.application.users.commands import CreateUserCommand
from src.application.users.dto import DeleteUserCommand
from src.application.users.usecases.create import CreateUserUseCase
from src.application.users.usecases.delete import DeleteUserUseCase
from src.infrastructure.authentication.password_hasher import PasswordHasher
from src.infrastructure.db.commiter import Commiter
from src.infrastructure.db.repositories.user import UserRepository


@convert_kwargs_to_snake_case
def resolve_create_user(
    _: Any,
    info: GraphQLResolveInfo,
    email: str,
    password: str,
    first_name: str | None = None,
    last_name: str | None = None,
) -> dict[str, Any]:
    db: SQLAlchemy = info.context["db"]

    usecase = CreateUserUseCase(
        commiter=Commiter(db=db),
        passwor_hasher=PasswordHasher(),
        user_repository=UserRepository(db=db),
    )

    command = CreateUserCommand(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )

    response = usecase.execute(command=command)

    return response


@convert_kwargs_to_snake_case
def resolve_delete_user(
    _: Any,
    info: GraphQLResolveInfo,
    id: UUID,
) -> None:
    db: SQLAlchemy = info.context["db"]

    usecase = DeleteUserUseCase(
        user_repository=UserRepository(db=db),
        commiter=Commiter(db=db),
    )

    command = DeleteUserCommand(id=id)

    usecase.execute(command=command)

    return None
