from typing import List, Union

from pydantic.main import BaseModel

from fast_tmp.amis.schema import BaseAmisModel

from .enums import TypeEnum


class Page(BaseAmisModel):
    type = TypeEnum.page
    body: Union[BaseAmisModel, List[BaseAmisModel]]
