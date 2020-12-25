from tortoise import Model, fields
# from fast_tmp.models import User, Group, Permission
from src.enums import Status


class Message(Model):
    info = fields.CharField(max_length=32, description="信息")
    e = fields.IntEnumField(Status)
