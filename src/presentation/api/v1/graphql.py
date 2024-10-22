from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, Response, jsonify, request

from src.infrastructure.db.database import db
from src.presentation.api.v1.schema import schema

explorer_html = ExplorerGraphiQL().html(None)  # type: ignore

app = Flask("__main__")


def graphql_server() -> tuple[str, int] | tuple[Response, int]:
    if request.method == "GET":
        return explorer_html, 200

    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value={"db": db},
        debug=app.debug,
    )

    status_code = 200 if success else 400

    return jsonify(result), status_code
