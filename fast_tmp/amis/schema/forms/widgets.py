from typing import Dict, List, Optional, Tuple, Union

from pydantic import HttpUrl
from pydantic.main import BaseModel

from fast_tmp.amis.schema.abstract_schema import _Action
from fast_tmp.amis.schema.forms.enums import ControlEnum, FormWidgetSize, ItemModel


# fixme:未来考虑更多的fields类型字段支持
class Column(BaseModel):
    """
    用于列表等的显示
    """

    name: str
    label: str


class AddControl(BaseModel):
    type: str = "text"
    name: str
    label: str


class Item(BaseModel):
    label: str
    value: Union[str, int]


class AbstractControl(Column):
    pass


class ItemValidation(BaseModel):  # 验证工具
    pass


class ItemValidationError(BaseModel):
    pass


# todo:等待完成
class Control(AbstractControl):
    """
    用户form表单等写入
    """

    type: ControlEnum = ControlEnum.text  # 把这个和schema获取的参数进行融合，保证schema获取的值可以使用
    name: str
    label: Optional[str]  # 表单项标签
    labelRemark: Optional[str]  # 表单项标签描述
    description: Optional[str]  # 描述
    placeholder: Optional[str]  # 描述
    inline: bool = False  # 内联样式
    submitOnChange: bool = False  # 是否该表单项值发生变化时就提交当前表单。
    disabled: bool = False
    disableOn: Optional[str]  # 配置规则查看https://baidu.gitee.io/amis/docs/components/form/formitem
    visible: bool = True
    visibleOn: Optional[str]  # 配置规则查看https://baidu.gitee.io/amis/docs/components/form/formitem
    required: bool = True
    requiredOn: Optional[str]
    hidden: bool = False  # 可使用条件配置如 this.number>1
    hiddenOn: Optional[str]  # 配置判定逻辑
    validations: Optional[Dict[str, Union[int, str]]]  # 注意，键值对请参考ValidateEnum
    validationErrors: Optional[
        Dict[str, str]
    ]  # 注意，键值对请参考ValidateEnum，举例："minimum": "同学，最少输入$1以上的数字哈",其中$1为该错误的数据
    className: Optional[str]  # 表单最外层类名
    inputClassName: Optional[str]  # 表单控制器类名
    labelClassName: Optional[str]  # label 的类名
    mode: ItemModel = ItemModel.normal
    size: FormWidgetSize = FormWidgetSize.md


class NumberItem(Control):
    type: ControlEnum = ControlEnum.number
    min: Optional[int]
    max: Optional[int]
    precision: int = 0  # 小数点后几位
    step: Optional[int]  # 选择的步长
    value: Optional[int]


class TextItem(Control):
    value: Optional[str]


class SelectOption(BaseModel):
    label: str
    value: Union[int, str]


class SelectItem(Control):
    type = ControlEnum.select
    options: Optional[List[Union[SelectOption, str, int]]]
    children: Optional[List[Union[SelectOption, str, int]]]  # 这个在树结构在考虑
    source: Optional[str]  # 通过数据源里面获取，也可以配置地址从远程获取，值格式为:options:[{label:..,value:...,}]
    multiple: bool = False  # 是否多选
    joinValues: Optional[bool]
    extractValue: Optional[bool]
    value: Optional[
        str
    ]  # 注意分割符保持一致,多选也可以配置返回数组格式，具体参考https://baidu.gitee.io/amis/docs/components/form/options#%E5%8A%A8%E6%80%81%E9%85%8D%E7%BD%AE
    searchable: bool = False  # 前端对选项是否启动搜索功能
    autoComplete: bool = True  # 是否对选项启动自动补全


class SelectItemCanModify(SelectItem):
    """
    可以修改选项值的选择器
    """

    creatable: bool = False  # 是否支持新增选项
    addControls: Tuple[AddControl, ...] = (
        AddControl(type="text", name="label", label="选项标题"),
        AddControl(type="text", name="value", label="选项值"),
    )  # 配置弹框信息，第一个为标题，第二个为选项值
    addApi: Optional[HttpUrl]  # 配置增加接口，如果为空则不会保存
    editable: bool = False  # 前端是否可编辑
    editControls: Tuple[AddControl, ...] = (
        AddControl(type="text", name="label", label="选项标题"),
        AddControl(type="text", name="value", label="选项值"),
    )  # 配置修改值的弹框信息
    editApi: Optional[HttpUrl]
    deleteApi: Optional[HttpUrl]  # 配置删除接口


class ArrayItem(Control):
    type: str = ControlEnum.array
    items: str = "text"  # 这个到时候改为枚举
    addable: bool = True  # 是否可新增
    removable: bool = True  # 是否可删除
    draggable: bool = False  # 是否可拖动排序，是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个$id 字段，具体请参考：https://baidu.gitee.io/amis/docs/components/form/array
    draggableTip: Optional[str]
    addButtonText: Optional[str]  # 新增按钮的文字
    minLength: Optional[int]  # 最短长度
    maxLength: Optional[int]  # 最长长度


class DatetimeItem(Control):
    type = ControlEnum.datetime
    value: Optional[str]
    format: str = "YYYY-MM-DD HH:mm:ss"  # 'X'为时间戳格式,参考文档：https://baidu.gitee.io/amis/zh-CN/docs/components/form/datetime
    inputFormat: str = "YYYY-MM-DD HH:mm:ss"  # 'X'为时间戳格式
    shortcuts: List[
        str
    ] = (
        []
    )  # "yesterday" ,"today", "tomorrow",now,{n}hoursago : n 小时前，例如：1daysago，下面用法相同,{n}hourslater : n 小时前，例如：1daysago
    utc: bool = False
    clearable: bool = True
    embed: bool = False  # fixme:学习内联如何使用
    timeConstrainst: bool = True  # 不知道干吗用的


class ButtonToolbar(AbstractControl):
    """
    按钮组
    """

    type = "button-toolbar"
    label: str = "按钮组"
    buttons: List[_Action]
