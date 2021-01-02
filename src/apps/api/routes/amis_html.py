# -*- encoding: utf-8 -*-
"""
@File    : amis_html.py
@Time    : 2021/1/1 14:56
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import HttpUrl
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from tortoise.contrib.pydantic import pydantic_model_creator

from fast_tmp.amis.schema.actions import DialogAction
from fast_tmp.amis.schema.crud import CRUD
from fast_tmp.amis.schema.form import Form
from fast_tmp.amis.schema.frame import Dialog
from fast_tmp.amis.utils import get_coulmns_from_pmc, get_coulmns_from_pqc
from fast_tmp.amis_router import AmisRouter
from fast_tmp.conf import settings
from src.models import Message
from src.schemas import ResMessageList, message_list_schema, message_schema

router = AmisRouter(prefix="/amis")


@router.get(
    "/message",
    view=CRUD(
        api=settings.SERVER_URL + router.prefix + "/message",
        columns=get_coulmns_from_pqc(message_list_schema),
    ),
    response_model=ResMessageList,
)
async def get_message():
    return {
        "total": await Message.all().count(),
        "items": await message_list_schema.from_queryset(Message.all()),
    }


@router.post(
    "/message",
    view=DialogAction(
        label="新增",
        dialog=Dialog(
            title="新增",
            body=Form(
                name="message_create",
                controls=get_coulmns_from_pmc(message_schema, add_type=True),
                api="http://127.0.0.1:8000/amis/message",
            ),
        ),
    ),
    response_model=message_schema,
)
async def create_message(message: message_schema):
    return await Message.create(**message.dict())
