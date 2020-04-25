from django.db import models
from datetime import datetime
from django.apps import apps

# Image = apps.get_model('image', 'Image')


class Party(models.Model):
    party_name = models.CharField(max_length=24)
    created_at = models.DateTimeField("date published", default=datetime.now())
    # images = models.ForeignKey('Image', on_delete=models.CASCADE)

    def has_expired(self):
        return self.created_at < timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f"{self.id} {self.party_name}"
