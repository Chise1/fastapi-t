# -*- encoding: utf-8 -*-
"""
@File    : global_settings.py
@Time    : 2020/12/20 23:44
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
import datetime

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DEFAULT_AUTH = True
EXPIRES_DELTA = datetime.timedelta(minutes=30)
AUTH_USER_MODEL = "User"
STATIC_URL = 'static'