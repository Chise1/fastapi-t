from fastapi_admin.models import AbstractAdminLog, AbstractPermission, AbstractRole, AbstractUser


class User(AbstractUser):
    last_login = fields.DatetimeField(description="Last Login", default=datetime.datetime.now)
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


class AdminLog(AbstractAdminLog):
    """
    must inheritance AbstractAdminLog
    """


class Config(Model):
    label = fields.CharField(max_length=200)
    key = fields.CharField(max_length=20)
    value = fields.JSONField()
    status: Status = fields.IntEnumField(Status, default=Status.on)

    def __str__(self):
        return f"{self.pk}#{self.label}"
