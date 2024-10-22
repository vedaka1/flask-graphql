from pathlib import Path

from ariadne import load_schema_from_path, make_executable_schema
from mutations import mutation
from queries import query

user_types = load_schema_from_path(Path(__file__).parent / "schemas" / "users.graphql")

type_defs = [
    user_types,
]

schema = make_executable_schema(type_defs, query, mutation)
