from django.db import models
from datetime import datetime

# Create your models here.


class Party(models.Model):
    party_name = models.CharField(max_length=24)
    created_at = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.party_name

    def has_expired(self):
        return self.created_at < timezone.now() - datetime.timedelta(days=1)
