from functools import lru_cache

from ariadne import ObjectType

from src.presentation.api.v1.queries.users import (
    resolve_get_user_by_id,
    resolve_get_users,
)


@lru_cache(1)
def get_queries() -> ObjectType:
    query = ObjectType("Query")

    query.set_field("getUsers", resolve_get_users)
    query.set_field("getUser", resolve_get_user_by_id)

    return query
