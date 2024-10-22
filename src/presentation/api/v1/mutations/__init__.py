from functools import lru_cache

from ariadne import ObjectType

from src.presentation.api.v1.mutations.users import (
    resolve_create_user,
    resolve_delete_user,
)


@lru_cache(1)
def get_mutations() -> ObjectType:
    mutation = ObjectType("Mutation")

    mutation.set_field("createUser", resolve_create_user)
    mutation.set_field("deleteUser", resolve_delete_user)

    return mutation
