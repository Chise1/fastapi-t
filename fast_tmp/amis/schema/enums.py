from enum import Enum


class LevelEnum(str, Enum):
    """
    按钮的显示类型
    """
    primary = "primary"
    secondary = "secondary"
    success = "success"
    warning = "warning"
    danger = "danger"
    light = "light"
    dark = "dark"
    link = "link"


class Icon(str, Enum):
    """
    按钮的图标
    """
    pass


class ActionTypeEnum(str, Enum):
    """
    触发按钮的类型
    """
    dialog = "dialog",  # 弹框
    ajax = "ajax"  # ajax请求

class TypeEnum(str, Enum):
    page = "page"
    crud = "crud"
    button="button"