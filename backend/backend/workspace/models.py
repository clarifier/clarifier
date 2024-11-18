from django.db import models


class Workspace(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    dimensions = models.ManyToManyField("profiling.Dimension")

    @classmethod
    def get_default_pk(cls):
        workspace, _ = cls.objects.get_or_create(
            name="default",
            defaults=dict(description="Default Workspace"),
        )
        return workspace.pk
