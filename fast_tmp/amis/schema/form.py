from typing import List, Optional

from pydantic import HttpUrl

from .abstract_schema import BaseAmisModel, Message, _Action
from .enums import TypeEnum
from .widgets import Control


class Form(BaseAmisModel):
    type = TypeEnum.form
    controls: List[Control]
    name: str
    title: str = "表单"
    submitText: str = "提交"
    # className:str
    # actions: Optional[List[_Action]]
    # messages: Optional[Message]#自定义返回信息加这个字段
    wrapWithPanel: bool = True
    api: HttpUrl
    initApi: Optional[HttpUrl]
    # interval: int = 3000??
    primaryField: str = "id"  # 设置主键
