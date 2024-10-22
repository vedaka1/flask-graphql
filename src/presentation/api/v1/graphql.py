from pathlib import Path

from ariadne import (
    MutationType,
    QueryType,
    graphql_sync,
    load_schema_from_path,
    make_executable_schema,
)
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, Response, jsonify, request

from src.infrastructure.db.database import db
from src.presentation.api.v1.views.users import (
    resolve_create_user,
    resolve_delete_user,
    resolve_get_user_by_id,
    resolve_get_users,
)

user_types = load_schema_from_path(Path(__file__).parent / "schemas" / "users.graphql")

type_defs = [
    user_types,
]

explorer_html = ExplorerGraphiQL().html(None)  # type: ignore

app = Flask("__main__")

query = QueryType()
mutation = MutationType()

query.set_field("users", resolve_get_users)
query.set_field("user", resolve_get_user_by_id)
mutation.set_field("createUser", resolve_create_user)
mutation.set_field("deleteUser", resolve_delete_user)

schema = make_executable_schema(type_defs, query, mutation)


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
