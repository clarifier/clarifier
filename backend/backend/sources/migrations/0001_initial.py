from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=128)),
                ("description", models.TextField(blank=True)),
                ("size", models.CharField(blank=True, max_length=128)),
                ("source", models.CharField(blank=True, max_length=128)),
                ("data", models.JSONField(default=dict)),
            ],
        ),
    ]
