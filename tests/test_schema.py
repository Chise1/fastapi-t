import json
from typing import NewType, Type, TypeVar

from pydantic.main import BaseModel
from pydantic.schema import schema


class B(BaseModel):
    x: int
    s: str


T = TypeVar("T", bound=B)


class C(B):
    pass


def s(a: B) -> T:
    pass


def b(a: Type[B]):
    pass


a: Type[C] = s(B())
r = schema([B], description="test_B")
print(json.dumps(r, indent=2))
v = {
    "fast_tmp.models.Permission.leaf": {
        "title": "Permission",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "minimum": 1, "maximum": 2147483647, "type": "integer"},
            "label": {"title": "Label", "maxLength": 128, "type": "string"},
            "model": {"title": "Model", "maxLength": 128, "type": "string"},
            "codename": {"title": "Codename", "maxLength": 128, "type": "string"},
        },
        "required": ["id", "label", "model", "codename"],
        "additionalProperties": False,
    },
    "fast_tmp.models.Group.4sx7nj": {
        "title": "Group",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "minimum": 1, "maximum": 2147483647, "type": "integer"},
            "label": {"title": "Label", "maxLength": 50, "type": "string"},
            "permissions": {
                "title": "Permissions",
                "type": "array",
                "items": {"$ref": "#/definitions/fast_tmp.models.Permission.leaf"},
            },
        },
        "required": ["id", "label", "permissions"],
        "additionalProperties": False,
    },
    "fast_tmp.models.User": {
        "title": "User",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "minimum": 1, "maximum": 2147483647, "type": "integer"},
            "username": {"title": "Username", "maxLength": 20, "type": "string"},
            "password": {"title": "Password", "maxLength": 200, "type": "string"},
            "is_active": {"title": "Is Active", "default": True, "type": "boolean"},
            "is_superuser": {"title": "Is Superuser", "default": False, "type": "boolean"},
            "groups": {
                "title": "Groups",
                "type": "array",
                "items": {"$ref": "#/definitions/fast_tmp.models.Group.4sx7nj"},
            },
        },
        "required": ["id", "username", "password", "groups"],
        "additionalProperties": False,
    },
}
