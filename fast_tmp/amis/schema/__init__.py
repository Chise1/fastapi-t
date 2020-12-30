from pydantic.main import BaseModel

from fast_tmp.amis.schema.enums import TypeEnum


class BaseAmisModel(BaseModel):
    type: TypeEnum
