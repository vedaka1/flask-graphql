from typing import Any
from uuid import UUID

from flask_sqlalchemy import SQLAlchemy
from graphql import GraphQLResolveInfo

from src.application.users.commands import CreateUserCommand, GetUserCommand
from src.application.users.dto import DeleteUserCommand
from src.application.users.usecases.create import CreateUserUseCase
from src.application.users.usecases.delete import DeleteUserUseCase
from src.application.users.usecases.get import GetUsersListUseCase, GetUserUseCase
from src.infrastructure.authentication.password_hasher import PasswordHasher
from src.infrastructure.db.commiter import Commiter
from src.infrastructure.db.repositories.user import UserRepository


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


def resolve_get_users(
    _: Any,
    info: GraphQLResolveInfo,
) -> list[dict[str, Any]]:
    db: SQLAlchemy = info.context["db"]

    usecase = GetUsersListUseCase(
        user_repository=UserRepository(db=db),
    )

    response = usecase.execute()

    return response


def resolve_get_user_by_id(
    _: Any,
    info: GraphQLResolveInfo,
    id: str,
) -> dict[str, Any] | None:
    db: SQLAlchemy = info.context["db"]

    usecase = GetUserUseCase(
        user_repository=UserRepository(db=db),
    )

    command = GetUserCommand(id=UUID(id))

    response = usecase.execute(command=command)

    return response
