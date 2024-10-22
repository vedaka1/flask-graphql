from flask import Flask

from .graphql import graphql_server


def init_routes(app: Flask) -> None:
    app.add_url_rule("/graphql", view_func=graphql_server, methods=["GET", "POST"])
