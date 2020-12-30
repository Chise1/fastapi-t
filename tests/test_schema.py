import json

from pydantic.main import BaseModel
from pydantic.schema import schema


class B(BaseModel):
    x: int
    s: str


r = schema([B], description="test_B")
print(json.dumps(r, indent=2))
v = {
    "type": "page",
    "body": [
        {
            "body": {
                "type": "crud",
                "api": "https://houtai.baidu.com/api/sample",
                "columns": [
                    {"name": "id", "label": "ID"},
                    {"name": "engine", "label": "Rendering engine"},
                    {"name": "browser", "label": "Browser"},
                    {"name": "platform", "label": "Platform(s)"},
                    {"name": "version", "label": "Engine version"},
                    {"name": "grade", "label": "CSS grade"},
                ],
            },
            "type": "page",
        },
        {
            "type": "crud",
            "api": "http://127.0.0.1:8000/admin/users",
            "columns": [
                {"name": "id", "label": "Id"},
                {"name": "username", "label": "Username"},
                {"name": "password", "label": "Password"},
                {"name": "is_active", "label": "Is Active"},
                {"name": "is_superuser", "label": "Is Superuser"},
                {"name": "groups", "label": "Groups"},
            ],
        },
    ],
}
