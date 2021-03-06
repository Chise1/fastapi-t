import aioredis
from aioredis import Redis


class AsyncRedisUtil:
    """
    异步redis操作
    """

    r = None  # type:Redis

    @classmethod
    async def init(cls, host="127.0.0.1", port=6379, password=None, db=0, **kwargs):
        cls.r = await aioredis.create_redis_pool(
            f"redis://{host}:{port}", password=password, db=db, **kwargs
        )
        return cls.r

    @classmethod
    async def _exp_of_none(cls, *args, exp_of_none, callback):
        if not exp_of_none:
            return await getattr(cls.r, callback)(*args)
        key = args[0]
        tr = cls.r.multi_exec()
        fun = getattr(tr, callback)
        exists = await cls.r.exists(key)
        if not exists:
            fun(*args)
            tr.expire(key, exp_of_none)
            ret, _ = await tr.execute()
        else:
            fun(*args)
            ret = (await tr.execute())[0]
        return ret

    @classmethod
    async def set(cls, key, value, exp=None):
        assert cls.r, "must call init first"
        await cls.r.set(key, value, expire=exp)

    @classmethod
    async def get(cls, key, default=None):
        assert cls.r, "must call init first"
        value = await cls.r.get(key)
        if value is None:
            return default
        return value

    @classmethod
    async def hget(cls, name, key, default=0):
        """
        缓存清除，接收list or str
        """
        assert cls.r, "must call init first"
        v = await cls.r.hget(name, key)
        if v is None:
            return default
        return v

    @classmethod
    async def get_or_set(cls, key, default=None, value_fun=None):
        """
        获取或者设置缓存
        """
        assert cls.r, "must call init first"
        value = await cls.r.get(key)
        if value is None and default:
            return default
        if value is not None:
            return value
        if value_fun:
            value, exp = await value_fun()
            await cls.r.set(key, value, expire=exp)
        return value

    @classmethod
    async def delete(cls, key):
        """
        缓存清除，接收list or str
        """
        assert cls.r, "must call init first"
        return await cls.r.delete(key)

    @classmethod
    async def sadd(cls, name, values, exp_of_none=None):
        assert cls.r, "must call init first"
        return await cls._exp_of_none(name, values, exp_of_none=exp_of_none, callback="sadd")

    @classmethod
    async def hset(cls, name, key, value, exp_of_none=None):
        assert cls.r, "must call init first"
        return await cls._exp_of_none(name, key, value, exp_of_none=exp_of_none, callback="hset")

    @classmethod
    async def hincrby(cls, name, key, value=1, exp_of_none=None):
        assert cls.r, "must call init first"
        return await cls._exp_of_none(name, key, value, exp_of_none=exp_of_none, callback="hincrby")

    @classmethod
    async def hincrbyfloat(cls, name, key, value, exp_of_none=None):
        assert cls.r, "must call init first"
        return await cls._exp_of_none(
            name, key, value, exp_of_none=exp_of_none, callback="hincrbyfloat"
        )

    @classmethod
    async def incrby(cls, name, value=1, exp_of_none=None):
        assert cls.r, "must call init first"
        return await cls._exp_of_none(name, value, exp_of_none=exp_of_none, callback="incrby")

    @classmethod
    async def close(cls):
        cls.r.close()
        await cls.r.wait_closed()
