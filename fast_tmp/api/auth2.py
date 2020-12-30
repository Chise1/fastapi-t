import json
from datetime import datetime
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel

from fast_tmp.conf import settings
from fast_tmp.core.amis_router import AmisRouter
from fast_tmp.core.mixins import AimsListMixin
from fast_tmp.schema import UserCreateSchema
from fast_tmp.templates_app import templates
from fast_tmp.utils.model import get_model_from_str

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.EXPIRES_DELTA
User = get_model_from_str(settings.AUTH_USER_MODEL)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

auth2_router = AmisRouter(prefix="/admin2")


from fastapi import Request
from fastapi.responses import HTMLResponse

from fast_tmp.amis.schema.amislist import AmisList


@auth2_router.get("/template", response_class=HTMLResponse)
async def template(
    request: Request,
):
    page = {
        "type": "page",
        "body": {
            "type": "crud",
            "api": "https://houtai.baidu.com/api/sample",
            "columns": [
                {"name": "id", "label": "ID"},
                {"name": "engine", "label": "Rendering engine"},
                {"name": "browser", "label": "Browser"},
                {"name": "platform", "label": "Platform(s)"},
                {"name": "version", "label": "Engine version"},
                {"name": "grade", "label": "CSS grade"},
            ],
        },
    }
    return templates.TemplateResponse(
        "admin/crud.html", {"request": request, "page": str(json.dumps(page))}
    )
