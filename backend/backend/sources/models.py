from django.db import models
from workspace.models import Workspace


class Source(models.Model):
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=128, blank=True)
    source = models.CharField(max_length=128, blank=True)
    data = models.JSONField(default=dict)
    workspace = models.ForeignKey(
        Workspace, default=Workspace.get_default_pk, on_delete=models.CASCADE
    )
