from dataclasses import dataclass
from typing import Any

from src.application.common.interfaces.commiter import CommiterInterface
from src.application.common.interfaces.password_hasher import PasswordHasherInterface
from src.application.users.commands import CreateUserCommand
from src.domain.users.entities import User
from src.domain.users.repositories import UserRepositoryInterface


@dataclass
class CreateUserUseCase:

    passwor_hasher: PasswordHasherInterface
    user_repository: UserRepositoryInterface
    commiter: CommiterInterface

    def execute(self, command: CreateUserCommand) -> dict[str, Any]:
        hashed_password = self.passwor_hasher.hash(password=command.password)

        user = User.create(
            email=command.email,
            first_name=command.first_name,
            last_name=command.last_name,
            hashed_password=hashed_password,
        )

        self.user_repository.create(user)

        self.commiter.commit()

        return {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
