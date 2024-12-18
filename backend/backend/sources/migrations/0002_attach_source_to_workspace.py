# Generated by Django 5.1.1 on 2024-11-18 14:44

import django.db.models.deletion
import workspace.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sources", "0001_initial"),
        ("workspace", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="workspace",
            field=models.ForeignKey(
                default=workspace.models.Workspace.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="workspace.workspace",
            ),
        ),
    ]
