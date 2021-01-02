from typing import List, Tuple, Type

from pydantic.main import BaseModel
from pydantic.schema import schema
from tortoise import Model

from fast_tmp.amis.schema.widgets import Column, Control


def get_coulmns_from_pqc(
    list_schema: Type[BaseModel],
    include: Tuple[str, ...] = None,
    exclude: Tuple[str, ...] = None,
    add_type=False,
    extra_fields=None,
):
    """
    从pydantic_queryset_creator创建的schema获取字段
    extra_field:额外的自定义字段
    """
    model_name = list_schema.__name__
    json_models = schema([list_schema])["definitions"]
    res: List[Column] = []
    for json_model in json_models:
        if json_model == model_name:
            items = json_models[json_model]["items"]
            for k, v in items.items():
                if k == "$ref":
                    m = json_models[v.split("/")[-1]]
                    fields = m["properties"]
                    for field_name in fields:
                        if include:
                            if field_name not in include:
                                continue
                        elif exclude:
                            if field_name in exclude:
                                continue
                        if add_type:
                            res.append(
                                Control(
                                    name=field_name,
                                    label=fields[field_name]["title"],
                                    type=pf_2_jsf(fields[field_name]["type"]),
                                )
                            )
                        else:
                            res.append(Column(name=field_name, label=fields[field_name]["title"]))
    if extra_fields:
        res.append(*extra_fields)
    return res


def pf_2_jsf(field_type: str) -> str:
    """
    把python的字段类型转为js的类型
    """
    if field_type == "integer":
        return "number"

    else:
        return "text"


def get_coulmns_from_pmc(
    model_schema: Type[Model],
    include: Tuple[str, ...] = None,
    exclude: Tuple[str, ...] = None,
    add_type: bool = False,
):
    """
    从pydantic_model_creator创建的schema获取字段
    """
    model_name = model_schema.__name__
    json_models = schema([model_schema])["definitions"]
    res: List[Column] = []
    for json_model in json_models:
        if json_model == model_name:
            items = json_models[json_model]["properties"]
            for k, v in items.items():
                if include:
                    if k not in include:
                        continue
                if exclude:
                    if k in exclude:
                        continue
                if add_type:
                    res.append(Control(name=k, label=v["title"], type=pf_2_jsf(v["type"])))
                else:
                    res.append(Column(name=k, label=v["title"]))
            break
    return res


# fixme:等待修复
def get_columns_from_str(
    fields: List[str], include: List[str] = None, exclude: List[str] = None, add_type: bool = False
) -> List[Column]:
    res = []
    for field in fields:
        res.append(Column(name=field, label=field))
    return res
