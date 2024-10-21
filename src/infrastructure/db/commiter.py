from flask_sqlalchemy import SQLAlchemy

from src.application.common.interfaces.commiter import CommiterInterface


class Commiter(CommiterInterface):

    def __init__(self, db: SQLAlchemy):
        self.db = db

    def commit(self) -> None:
        self.db.session.commit()

    def rollback(self) -> None:
        self.db.session.rollback()

    def close(self) -> None:
        self.db.session.close()
