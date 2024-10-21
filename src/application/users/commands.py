from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateUserCommand:
    email: str
    password: str
    first_name: str | None
    last_name: str | None
    is_verified: bool = False


@dataclass
class GetUserCommand:
    id: UUID
