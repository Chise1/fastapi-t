from typing import Type

from tortoise import fields, models

from fast_tmp.utils.password import make_password, verify_password


# 采用引用方式使用，只要再主models里面引入这三个model，就能创建对应表
class User(models.Model):
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=200, )
    is_active = fields.BooleanField(default=True, )
    is_superuser = fields.BooleanField(default=False)

    def set_password(self, raw_password: str):
        """
        设置密码
        :param raw_password:
        :return:
        """
        self.password = make_password(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        """
        验证密码
        :param raw_password:
        :return:
        """
        return verify_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Permission(models.Model):
    label = fields.CharField(max_length=128)
    model = fields.CharField(max_length=128)
    codename = fields.CharField(max_length=128)

    def __str__(self):
        return self.label

    @classmethod
    def make_permission(cls, model: Type[models.Model], ):
        """
        生成model对应的权限
        """
        # todo:生成对应默认权限


class Group(models.Model):
    label = fields.CharField(max_length=50)
    users = fields.ManyToManyField("models.User")
    permissions = fields.ManyToManyField("models.Permission")

    def __str__(self):
        return self.label
