from fast_tmp.models.enums import IntegerChoices


class Status(IntegerChoices):
    """
    状态
    """

    on = 1, "开启"
    off = 0, "关闭"


x = Status.choices
