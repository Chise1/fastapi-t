from fast_tmp.models import AbstractPermission, AbstractRole, AbstractUser
from tortoise import fields,Model
from tortoise import timezone
from src.enums import Status
class Message(Model):
    info=fields.CharField(max_length=32,description='信息')
class User(AbstractUser):
    last_login = fields.DatetimeField(description="Last Login", default=timezone.datetime.now)
    avatar = fields.CharField(max_length=200, default="")
    intro = fields.TextField(default="")
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}#{self.username}"

    def rowVariant(self) -> str:
        if not self.is_active:
            return "warning"
        return ""

    def cellVariants(self) -> dict:
        if self.is_active:
            return {
                "intro": "info",
            }
        return {}

    class PydanticMeta:
        computed = ("rowVariant", "cellVariants")


class Permission(AbstractPermission):
    """
    must inheritance AbstractPermission
    """


class Role(AbstractRole):
    """
    must inheritance AbstractRole
    """



# class Config(Model):
#     label = fields.CharField(max_length=200)
#     key = fields.CharField(max_length=20)
#     value = fields.JSONField()
#     status: Status = fields.IntEnumField(Status.choices, default=Status.on)
#
#     def __str__(self):
#         return f"{self.pk}#{self.label}"
