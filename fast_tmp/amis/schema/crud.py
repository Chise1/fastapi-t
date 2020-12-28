from typing import List
from pydantic import HttpUrl
from . import TypeEnum, BaseAmisModel
from .widgets import Column


class CRUD(BaseAmisModel):
    type = TypeEnum.crud
    api: HttpUrl
    columns: List[Column]
