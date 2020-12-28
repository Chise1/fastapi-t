import os
import sys

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fast_tmp.conf import settings
from fast_tmp.jinja_extension.tags import register_tags

paths = sys.path


def get_dir():
    return os.path.dirname(__file__)


DIR = get_dir()

template_path = os.path.join(DIR, 'templates')
templates = Jinja2Templates(directory=template_path)
register_tags(templates)


def create_aapp():
    fast_tmp_app = FastAPI(debug=settings.DEBUG)
    if settings.DEBUG:
        fast_tmp_app.mount("/static", StaticFiles(directory=os.path.join(DIR, "static")), name="static")
    else:
        fast_tmp_app.mount("/static", StaticFiles(directory=os.path.join(settings.BASE_DIR, settings.STATIC_ROOT)),
                           name="static")
