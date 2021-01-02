from enum import Enum


class ButtonLevelEnum(str, Enum):
    """
    按钮的显示类型
    """

    info = "info"
    primary = "primary"
    secondary = "secondary"
    success = "success"
    warning = "warning"
    danger = "danger"
    light = "light"
    dark = "dark"
    link = "link"
    default = "default"


class Icon(str, Enum):
    """
    按钮的图标
    """

    pass


class ActionTypeEnum(str, Enum):
    """
    触发按钮的类型
    """

    dialog = "dialog"  # 弹框
    ajax = "ajax"  # ajax请求
    copy = "copy"  # 复制文本
    reload = "reload"  # 重载空间
    link = "link"  # 链接
    url = "url"
    drawer = "drawer"
    confirm = "confirm"
    cancel = "cancel"
    prev = "prev"
    next = "next"
    close = "close"


class TypeEnum(str, Enum):
    page = "page"
    crud = "crud"
    button = "button"
    action = "action"  # 行为按钮
    form = "form"
    operation = "operation"  # 这是啥？？


class WidgetSize:
    lg = "lg"  # 大
    md = "md"  # 中,默认值
    sm = "sm"  # 小
    xs = "xs"  # 极小


class ButtonSize(
    str,
    Enum,
):
    lg = "lg"  # 大
    md = "md"  # 中,默认值
    sm = "sm"  # 小
    xs = "xs"  # 极小


class DialogSize(str, Enum):
    full = "full"  # 全屏
    lg = "lg"  # 大
    md = "md"  # 中,默认值
    sm = "sm"  # 小
    xl = "xl"
    xs = "xs"  # 极小


class FormWidgetSize(
    str,
    Enum,
):
    full = "full"
    lg = "lg"  # 大
    md = "md"  # 中,默认值
    sm = "sm"  # 小
    xs = "xs"  # 极小


class ControlEnum(str, Enum):
    text = "text"


class FormModel(str, Enum):
    horizontal = "horizontal"
    inline = "inline"
    normal = "normal"
