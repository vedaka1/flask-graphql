from abc import ABC, abstractmethod
from uuid import UUID

from flask_sqlalchemy.session import Session

from src.domain.users.entities import User


class UserRepositoryInterface(ABC):

    def ___init__(self, session: Session) -> None:
        self.session = session

    @abstractmethod
    def create(self, user: User) -> None: ...

    @abstractmethod
    def get_many(self) -> list[User]: ...

    @abstractmethod
    def delete(self, id: UUID) -> None: ...

    @abstractmethod
    def get_by_id(self, id: UUID) -> User | None: ...
