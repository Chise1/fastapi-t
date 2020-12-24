from fast_tmp.redis import AsyncRedisUtil
from fastapi import FastAPI
from tortoise import Tortoise
from fastapi.middleware import Middleware
from src import rearq, settings
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
@rearq.on_startup
async def on_startup():
    await AsyncRedisUtil.init(**settings.REDIS)
    await Tortoise.init(config=settings.TORTOISE_ORM)


@rearq.on_shutdown
async def on_shutdown():
    await AsyncRedisUtil.close()
    await Tortoise.close_connections()


def init_app(main_app:FastAPI):
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
    Tortoise.init_models(settings.TORTOISE_ORM['apps']['models']['models'],'models')

    # fixme:
    # 初始化tortoise的model结构之后再引入一些包
    # fixme:引入一些包
    ...

    # fixme:等待修复
    # fast_app.mount("/admin", admin_app)
    # fast_app.mount("/api", api_app)
    # fast_app.mount("/docs", docs_app)
    # fast_app.mount("/script", script_app)
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Sentry的插件
    # fast_app.add_middleware(SentryAsgiMiddleware)

    register_tortoise(fast_app, config=settings.TORTOISE_ORM)
    init_app(fast_app)

    return fast_app
