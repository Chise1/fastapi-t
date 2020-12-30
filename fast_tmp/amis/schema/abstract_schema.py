from typing import Optional

from . import BaseAmisModel
from .enums import ActionTypeEnum, ButtonLevelEnum, ButtonSize, TypeEnum


class _Action(BaseAmisModel):
    type = TypeEnum.action
    label: str
    actionType: ActionTypeEnum
    icon: Optional[str] = None
    size: ButtonSize = ButtonSize.md
    level: ButtonLevelEnum = ButtonLevelEnum.primary
    tooltip: Optional[str] = None  # 鼠标挪上去的提示
