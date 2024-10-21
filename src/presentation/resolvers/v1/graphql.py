from pathlib import Path

from ariadne import MutationType, QueryType, graphql_sync, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request

from src.infrastructure.db.database import db
from src.presentation.resolvers.v1.views.users import (
    resolve_create_user,
    resolve_delete_user,
    resolve_get_user_by_id,
    resolve_get_users,
)

type_defs = open(Path(__file__).parent / "schemas" / "users.graphql").read()
explorer_html = ExplorerGraphiQL().html(None)
app = Flask("__main__")

query = QueryType()
mutation = MutationType()

query.set_field("users", resolve_get_users)
query.set_field("user", resolve_get_user_by_id)
mutation.set_field("createUser", resolve_create_user)
mutation.set_field("deleteUser", resolve_delete_user)

schema = make_executable_schema(type_defs, query, mutation)


def graphql_server():
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
