from typing import Union, List

from fast_tmp.amis.schema import BaseAmisModel
from .enums import TypeEnum

class Page(BaseAmisModel):
    type = TypeEnum.page
    body: Union[BaseAmisModel, List[BaseAmisModel]]
