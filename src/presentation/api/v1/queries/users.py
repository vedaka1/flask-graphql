from typing import Any
from uuid import UUID

from ariadne import convert_kwargs_to_snake_case
from flask_sqlalchemy import SQLAlchemy
from graphql import GraphQLResolveInfo

from src.application.users.commands import GetUserCommand
from src.application.users.usecases.get import GetUsersListUseCase, GetUserUseCase
from src.infrastructure.db.repositories.user import UserRepository


@convert_kwargs_to_snake_case
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


@convert_kwargs_to_snake_case
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
