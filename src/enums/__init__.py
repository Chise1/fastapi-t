from fast_tmp.utils.base_enums import IntEnumType


class Status(IntEnumType):
    """
    状态
    """

    on = 1, "开启"
    off = 0, "关闭"
