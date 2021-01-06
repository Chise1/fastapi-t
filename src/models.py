from tortoise import Model, fields

from src.enums import Status, Status2


class MessageUser(Model):
    nickname = fields.CharField(max_length=32)


class MessageM2M(Model):
    msg = fields.CharField(max_length=128)


class MessageM2M2(Model):
    msg = fields.CharField(max_length=128)
    messages = fields.ManyToManyField("models.Message")


class MessageOther(Model):
    other_info = fields.CharField(max_length=32)


class Message(Model):
    ix = fields.IntField(verbose_name="message_ix", default=10)
    info = fields.CharField(max_length=32, description="信息")
    error_info = fields.IntEnumField(Status)
    error_info_str = fields.CharEnumField(Status2)
    message_user = fields.ForeignKeyField("models.MessageUser")
    send_time = fields.DatetimeField()
    send_date = fields.DateField()
    d = fields.CharField(max_length=12)
    message_m2ms = fields.ManyToManyField("models.MessageM2M")
    js = fields.JSONField()
    fl = fields.FloatField()
    uuid = fields.UUIDField()
    td = fields.TimeDeltaField()
    other_field = fields.OneToOneField("models.MessageOther")
    text = fields.TextField()
    small_int = fields.SmallIntField()
    big_int = fields.BigIntField()
    biny = fields.BinaryField()
    dec = fields.DecimalField(max_digits=10, decimal_places=3)
    bl = fields.BooleanField(default=False)
    b_message: fields.ForeignKeyRelation['Bmessage']


class Amessage(Model):
    messages = fields.ForeignKeyField("models.Message")


class Bmessage(Model):
    messages = fields.ForeignKeyField("models.Message")

class Cmessage(Model):
    id=fields.OneToOneField("Message",pk=True)

class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    events: fields.ReverseRelation["Event"]

    def __str__(self):
        return self.name


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament",
        related_name="events",
        on_delete=fields.CASCADE,
    )
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )

    def __str__(self):
        return self.name


class Address(Model):
    city = fields.CharField(max_length=64)
    street = fields.CharField(max_length=128)

    event: fields.OneToOneRelation[Event] = fields.OneToOneField(
        "models.Event", on_delete=fields.CASCADE, related_name="address", pk=True
    )

    def __str__(self):
        return f"Address({self.city}, {self.street})"


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    events: fields.ManyToManyRelation[Event]

    def __str__(self):
        return self.name
