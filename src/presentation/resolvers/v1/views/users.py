from uuid import UUID

from flask_sqlalchemy import SQLAlchemy

from src.application.users.commands import CreateUserCommand, GetUserCommand
from src.application.users.dto import DeleteUserCommand
from src.application.users.usecases.create import CreateUserUseCase
from src.application.users.usecases.delete import DeleteUserUseCase
from src.application.users.usecases.get import GetUsersListUseCase, GetUserUseCase
from src.infrastructure.authentication.password_hasher import PasswordHasher
from src.infrastructure.db.commiter import Commiter
from src.infrastructure.db.repositories.user import UserRepository


def resolve_create_user(
    _,
    info,
    email: str,
    password: str,
    first_name: str | None = None,
    last_name: str | None = None,
):
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
    _,
    info,
    id: UUID,
):
    db: SQLAlchemy = info.context["db"]

    usecase = DeleteUserUseCase(
        commiter=Commiter(db=db),
        user_repository=UserRepository(db=db),
    )

    command = DeleteUserCommand(id=id)

    response = usecase.execute(command=command)

    return response


def resolve_get_users(
    _,
    info,
):
    db: SQLAlchemy = info.context["db"]

    usecase = GetUsersListUseCase(
        user_repository=UserRepository(db=db),
    )

    response = usecase.execute()

    return response


def resolve_get_user_by_id(
    _,
    info,
    id: str,
):
    db: SQLAlchemy = info.context["db"]

    usecase = GetUserUseCase(
        user_repository=UserRepository(db=db),
    )

    command = GetUserCommand(id=UUID(id))

    response = usecase.execute(command=command)

    return response
