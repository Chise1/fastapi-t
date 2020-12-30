from typing import List, Union

from pydantic import HttpUrl

from . import BaseAmisModel, TypeEnum
from .actions import _Action
from .widgets import Column


class CRUD(BaseAmisModel):
    type = TypeEnum.crud
    api: HttpUrl
    # 可以在后面跟上按钮，则默认每一行都有按钮，
    # 参考：https://baidu.gitee.io/amis/docs/components/dialog?page=1
    columns: List[Union[Column, _Action]]
