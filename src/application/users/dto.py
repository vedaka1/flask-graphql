from dataclasses import dataclass
from uuid import UUID


@dataclass
class UserOut:
    id: UUID
    email: str
    first_name: str | None
    last_name: str | None
    is_verified: bool


@dataclass
class DeleteUserCommand:
    id: UUID
