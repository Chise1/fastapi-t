from pydantic.main import BaseModel
from . import TypeEnum
from .crud import CRUD


class List(BaseModel):
    type = TypeEnum.page
    body: CRUD
