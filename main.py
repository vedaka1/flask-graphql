from flask import Flask

from src.infrastructure.db.database import init_db, init_flask_migrations
from src.presentation.resolvers.v1.router import init_routes


def create_app() -> Flask:
    app = Flask(__name__)

    init_db(app=app)
    init_routes(app=app)
    init_flask_migrations(app=app)

    return app
