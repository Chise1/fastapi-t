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
