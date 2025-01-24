from typing import Any

from flask import Flask


def app_error_handler(e: Exception) -> dict[str, Any]:
    data = {
        'errors': {
            'code': 1,
            'message': str(e),
        }
    }
    return data


def register_error_handlers(app: Flask) -> None:
    app.register_error_handler(Exception, app_error_handler)
