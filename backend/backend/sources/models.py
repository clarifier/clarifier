from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    size = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
    data = models.JSONField()
