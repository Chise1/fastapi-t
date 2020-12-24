from typing import Type

from tortoise import Model, fields, timezone

from src.enums import Status


class Message(Model):
    info = fields.CharField(max_length=32, description="信息")


class User(Model):
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(
        max_length=200,
    )
    is_active = fields.BooleanField(
        default=True,
    )
    is_superuser = fields.BooleanField(default=False)

    def __str__(self):
        return self.username


class Permission(Model):
    label = fields.CharField(max_length=128)
    model = fields.CharField(max_length=128)
    codename = fields.CharField(max_length=128)

    def __str__(self):
        return self.label

    @classmethod
    def make_permission(
        cls,
        model: Type[Model],
    ):
        """
        生成model对应的权限
        """
        # todo:生成对应默认权限


class Group(Model):
    label = fields.CharField(max_length=50)
    users = fields.ManyToManyField("models.User")
    permissions = fields.ManyToManyField("models.Permission")

    def __str__(self):
        return self.label


class Config(Model):
    label = fields.CharField(max_length=200)
    key = fields.CharField(max_length=20)
    value = fields.JSONField()
    status: Status = fields.IntEnumField(Status, default=Status.on)

    def __str__(self):
        return f"{self.pk}#{self.label}"
