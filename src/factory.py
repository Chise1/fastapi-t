from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from fast_tmp.conf import settings
from fast_tmp.exception_handler import validation_exception_handler
from fast_tmp.redis import AsyncRedisUtil
from src import rearq


@rearq.on_startup
async def on_startup():
    await AsyncRedisUtil.init(**settings.REDIS)
    await Tortoise.init(config=settings.TORTOISE_ORM)


@rearq.on_shutdown
async def on_shutdown():
    await AsyncRedisUtil.close()
    await Tortoise.close_connections()


def init_app(main_app: FastAPI):
    @main_app.on_event("startup")
    async def startup() -> None:
        await AsyncRedisUtil.init(**settings.REDIS)
        await rearq.init()

    @main_app.on_event("shutdown")
    async def shutdown() -> None:
        await AsyncRedisUtil.close()
        await rearq.close()


def create_app():
    fast_app = FastAPI(debug=settings.DEBUG)
    Tortoise.init_models(settings.TORTOISE_ORM["apps"]["models"]["models"], "models")
    # 一定要先把model初始化之后再引入路由，不然外键字段无法被使用到
    from fast_tmp.factory import create_fast_tmp_app

    from .apps.api.routes.amis_html import router as amis_test_router

    fast_tmp_app = create_fast_tmp_app()
    fast_app.include_router(
        amis_test_router,
    )
    fast_app.mount(settings.ADMIN_URL, fast_tmp_app)

    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Sentry的插件
    # fast_app.add_middleware(SentryAsgiMiddleware)
    # 替换报错信息
    fast_app.add_exception_handler(RequestValidationError, validation_exception_handler)
    register_tortoise(fast_app, config=settings.TORTOISE_ORM)
    init_app(fast_app)
    return fast_app
