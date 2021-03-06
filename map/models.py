from django.db import models
from uuid import uuid4
from django.contrib.postgres.fields import JSONField

class Map(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    data = JSONField()
