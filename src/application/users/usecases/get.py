from calendar import c
from dataclasses import dataclass
from typing import Any

from src.application.users.commands import GetUserCommand
from src.application.users.dto import UserOut
from src.domain.users.repositories import UserRepositoryInterface


@dataclass
class GetUsersListUseCase:

    user_repository: UserRepositoryInterface

    def execute(self) -> list[dict[str, Any]]:

        users = self.user_repository.get_many()
        return [
            {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_verified": user.is_verified,
            }
            for user in users
        ]


@dataclass
class GetUserUseCase:

    user_repository: UserRepositoryInterface

    def execute(self, command: GetUserCommand) -> dict[str, Any] | None:

        user = self.user_repository.get_by_id(command.id)

        return (
            {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_verified": user.is_verified,
            }
            if user
            else None
        )
