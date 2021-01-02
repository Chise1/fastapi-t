from typing import Optional

from pydantic.main import BaseModel

from fast_tmp.amis.schema.enums import ControlEnum, FormWidgetSize


class Column(BaseModel):
    """
    用于列表等的显示
    """

    name: str
    label: str


# todo:等待完成
class Control(Column):
    """
    用户form表单等写入
    """

    type: str = "text"  # 把这个和schema获取的参数进行融合，保证schema获取的值可以使用
    name: str
    label: str
    size: FormWidgetSize = FormWidgetSize.md
    placeholder: Optional[str] = None
    labelRemark: Optional[str] = None
    disableOn: str = None  # 配置规则查看https://baidu.gitee.io/amis/docs/components/form/formitem
    hidden: bool = False  # 可使用条件配置如 this.number>1
    required: bool = True
