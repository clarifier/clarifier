from django.db import models


class DimensionGroup(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    group = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = (
            "name",
            "group",
        )


class Dimension(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    group = models.ForeignKey(DimensionGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "name",
            "group",
        )
