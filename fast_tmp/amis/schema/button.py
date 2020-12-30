from . import BaseAmisModel, TypeEnum
from .enums import ActionTypeEnum, Ty


class Button(BaseAmisModel):
    type = TypeEnum.button
    label: str
    actionType: ActionTypeEnum
