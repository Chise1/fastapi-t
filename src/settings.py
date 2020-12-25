import logging
import os
import sys

from dotenv import load_dotenv

load_dotenv()
DEBUG = os.getenv("DEBUG") == "True"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_SECRET = os.getenv("API_SECRET")
ADMIN_SECRET = os.getenv("ADMIN_SECRET")
SECRET_KEY = os.getenv("SECRET_KEY")
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", 3306)
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

REARQ = {
    "redis_host": REDIS_HOST,
    "redis_port": REDIS_PORT,
    "redis_password": REDIS_PASSWORD,
    "redis_db": 1,
}
REDIS = {
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "password": REDIS_PASSWORD,
    "db": 2,
    "encoding": "utf-8",
}

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": DB_HOST,
                "port": DB_PORT,
                "user": DB_USER,
                "password": DB_PASSWORD,
                "database": DB_NAME,
                "echo": os.getenv("DB_ECHO") == "True",
                "maxsize": 10,
            },
        },
    },
    "apps": {
        "models": {
            "models": ['fast_tmp.models', "src.models", "aerich.models", ],
            "default_connection": "default",
        },
    },
}
