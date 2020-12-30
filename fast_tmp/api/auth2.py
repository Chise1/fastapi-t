import json
from datetime import datetime
from typing import Optional, Type

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from pydantic.schema import schema
from tortoise.contrib.pydantic import pydantic_queryset_creator

from fast_tmp.amis.schema.crud import CRUD
from fast_tmp.amis.utils import get_columns, get_coulmns_from_list_schema
from fast_tmp.conf import settings
from fast_tmp.core.amis_router import AmisRouter
from fast_tmp.utils.model import get_model_from_str

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.EXPIRES_DELTA
User = get_model_from_str(settings.AUTH_USER_MODEL)

auth2_router = AmisRouter(prefix="/admin2")

users_schema = pydantic_queryset_creator(User)


class A(BaseModel):
    items: users_schema


print(settings.SERVER_URL + settings.ADMIN_URL + "/users")


@auth2_router.get(
    "/users",
    view=CRUD(
        api=settings.SERVER_URL + settings.ADMIN_URL + auth2_router.prefix + "/users",
        columns=get_coulmns_from_list_schema(users_schema),
    ),
    response_model=A,
)
async def users():
    return {"items": await users_schema.from_queryset(User.all())}
