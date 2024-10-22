from ariadne import QueryType

from src.presentation.api.v1.queries.users import (
    resolve_get_user_by_id,
    resolve_get_users,
)

query = QueryType()

query.set_field("users", resolve_get_users)
query.set_field("user", resolve_get_user_by_id)
