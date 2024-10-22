from pathlib import Path

from ariadne import load_schema_from_path, make_executable_schema

from src.presentation.api.v1.mutations import get_mutations
from src.presentation.api.v1.queries import get_queries

user_types = load_schema_from_path(Path(__file__).parent / "schemas" / "users.graphql")

type_defs = [
    user_types,
]

queries = get_queries()
mutations = get_mutations()

schema = make_executable_schema(type_defs, queries, mutations)
