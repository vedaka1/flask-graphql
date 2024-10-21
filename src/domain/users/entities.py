from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class User:
    id: UUID
    email: str
    hashed_password: str
    first_name: str | None
    last_name: str | None
    is_verified: bool

    @staticmethod
    def create(
        email: str,
        hashed_password: str,
        first_name: str | None = None,
        last_name: str | None = None,
        is_verified: bool = False,
    ) -> "User":
        return User(
            id=uuid4(),
            email=email,
            hashed_password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            is_verified=is_verified,
        )
