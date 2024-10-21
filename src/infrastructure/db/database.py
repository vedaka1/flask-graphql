from functools import lru_cache

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from src.infrastructure.settings import settings


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()


@lru_cache(1)
def init_db(app: Flask) -> SQLAlchemy:
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.db.DB_URL

    db.init_app(app)

    return db


@lru_cache(1)
def init_flask_migrations(app: Flask) -> Migrate:

    migrate.init_app(app, db)

    return migrate
