from dataclasses import dataclass
from typing import Any

from src.application.common.interfaces.commiter import CommiterInterface
from src.application.users.dto import DeleteUserCommand
from src.domain.users.repositories import UserRepositoryInterface


@dataclass
class DeleteUserUseCase:

    user_repository: UserRepositoryInterface
    commiter: CommiterInterface

    def execute(self, command: DeleteUserCommand) -> None:
        self.user_repository.delete(command.id)

        self.commiter.commit()

        return None
