from tortoise.models import Model
from tortoise import fields

import pendulum


class Session(Model):
    """
    Used to group Entries
    """

    id = fields.UUIDField(pk=True)
    description = fields.TextField()
    start = fields.DatetimeField(null=True)
    end = fields.DatetimeField(null=True)

    class Meta:
        table = "sessions"

    def __str__(self):
        return self.description


class Reporter(Model):
    """
    Which plugin reported the entry.
    """

    id = fields.UUIDField(pk=True)
    slug = fields.CharField(max_length=100, index=True)
    description = fields.TextField()
    enabled = fields.BooleanField(default=True)

    class Meta:
        table = "reporters"

    def __str__(self):
        return f"{self.description} ({self.slug})"


class Entry(Model):
    """
    A single entry in the worklog. Can be grouped using Sessions.
    """

    id = fields.UUIDField(pk=True)
    description = fields.TextField()
    timestamp = fields.DatetimeField(default=pendulum.now, index=True)
    session = fields.ForeignKeyField(
        "models.Session", related_name="entries", null=True
    )
    reporter = fields.ForeignKeyField(
        "models.Reporter", related_name="entries", null=True
    )

    class Meta:
        table = "entries"

    def __str__(self):
        return self.description
