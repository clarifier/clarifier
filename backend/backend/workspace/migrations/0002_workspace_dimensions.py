# Generated by Django 5.1.1 on 2024-11-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiling", "0003_add_drl_dimensions"),
        ("workspace", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workspace",
            name="dimensions",
            field=models.ManyToManyField(to="profiling.dimension"),
        ),
    ]
