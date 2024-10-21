from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CommiterInterface(ABC):
    @abstractmethod
    def commit(self) -> None: ...

    @abstractmethod
    def rollback(self) -> None: ...

    @abstractmethod
    def close(self) -> None: ...
