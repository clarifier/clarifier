from django.db import migrations


def populate_dimension_group_and_dimensions(apps, schema_editor):
    DimensionGroup = apps.get_model("profiling", "DimensionGroup")
    Dimension = apps.get_model("profiling", "Dimension")

    # Create DimensionGroup
    group = DimensionGroup.objects.create(
        name="ABC",
        description="The ABC of data: A classifying framework for data readiness (2020)",
    )

    # Create DimensionGroups ABC and Dimensions
    bands = [
        {
            "name": "Band A",
            "dimensions": [
                "Interpretable Values",
                "Feature Scaling",
                "Outlier Detection",
                "Feature Selection",
                "Coverage Gap Detection",
            ],
        },
        {
            "name": "Band B",
            "dimensions": [
                "Column Types",
                "Missing Values",
                "Inconsistent Data Entries",
                "Duplicated Records",
                "Meaningful Values",
            ],
        },
        {
            "name": "Band C",
            "dimensions": [
                "Parseability",
                "Data storage",
                "Decoding",
                "Data Formats",
                "Disjoint Datasets",
            ],
        },
    ]

    for band in bands:
        band_group = DimensionGroup.objects.create(
            group=group,
            name=band["name"],
            description=band["name"],
        )
        for dimension in band["dimensions"]:
            Dimension.objects.create(
                group=band_group, name=dimension, description=dimension
            )


def rollback_dimension_group_and_dimensions(apps, schema_editor):
    DimensionGroup = apps.get_model("profiling", "DimensionGroup")
    Dimension = apps.get_model("profiling", "Dimension")

    # Get the group to delete dimensions and the group itself
    try:
        group = DimensionGroup.objects.get(name="ABC")
        # Delete all dimensions related to the group
        Dimension.objects.filter(group=group).delete()
        # Delete the group
        group.delete()
    except DimensionGroup.DoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [
        # Replace '0001_initial' with the actual name of the migration
        # that creates the DimensionGroup and Dimension models
        ("profiling", "0002_add_dama_dimensions"),
    ]

    operations = [
        migrations.RunPython(
            populate_dimension_group_and_dimensions,
            rollback_dimension_group_and_dimensions,
        ),
    ]
