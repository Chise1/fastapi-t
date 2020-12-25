from typing import Type

from tortoise import Model, fields, timezone

from src.enums import Status


class Message(Model):
    info = fields.CharField(max_length=32, description="信息")
    e = fields.IntEnumField(Status.choices)
