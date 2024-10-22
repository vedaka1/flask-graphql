from pathlib import Path

from ariadne import (
    MutationType,
    QueryType,
    load_schema_from_path,
    make_executable_schema,
)

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

query = QueryType()
mutation = MutationType()

query.set_field("users", resolve_get_users)
query.set_field("user", resolve_get_user_by_id)

mutation.set_field("createUser", resolve_create_user)
mutation.set_field("deleteUser", resolve_delete_user)

schema = make_executable_schema(type_defs, query, mutation)
