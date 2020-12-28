import os
import sys
from fastapi import FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED

from fast_tmp.api.auth import auth_router
from fast_tmp.conf import settings
from src.apps.api import ErrorException

paths = sys.path


def get_dir():
    return os.path.dirname(__file__)


DIR = get_dir()


# fixme:等待启用
async def http_exception_handler(request: Request, exc: HTTPException):
    print(exc.status_code)
    return exc
    # if exc.status_code == HTTP_401_UNAUTHORIZED:
    #     ret = TokenInvalid(msg=exc.detail).dict()
    # elif exc.status_code == HTTP_403_FORBIDDEN:
    #     ret = Forbidden(msg=exc.detail).dict()
    # else:
    #     logger.error(f"HTTPException: {exc.detail}", exc_info=True)
    #     ret = UnKnownError(msg=exc.detail).dict()
    # if settings.DEBUG:
    #     return ORJSONResponse(ret)
    # return AesResponse(ret)


# fixme:等待启用
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


# fixme:等待启用
async def error_exception_handler(request: Request, exc: ErrorException):
    print(exc)
    return exc


def create_fast_tmp_app():
    fast_tmp_app = FastAPI(debug=settings.DEBUG)
    if settings.DEBUG:
        fast_tmp_app.mount("/static", StaticFiles(directory=os.path.join(DIR, "static")), name="static")
    else:
        fast_tmp_app.mount("/static", StaticFiles(directory=os.path.join(settings.BASE_DIR, settings.STATIC_ROOT)),
                           name="static")
    fast_tmp_app.include_router(auth_router)
    # fast_tmp_app.add_exception_handler(
    #     HTTPException, http_exception_handler
    # )
    # fast_tmp_app.add_exception_handler(
    #     ErrorException, error_exception_handler
    # )
    # fast_tmp_app.add_exception_handler(
    #     RequestValidationError, validation_exception_handler
    # )
    return fast_tmp_app
