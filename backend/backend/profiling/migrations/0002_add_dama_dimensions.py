from django.db import migrations


def populate_dimension_group_and_dimensions(apps, schema_editor):
    DimensionGroup = apps.get_model("profiling", "DimensionGroup")
    Dimension = apps.get_model("profiling", "Dimension")

    # Create DimensionGroup
    group = DimensionGroup.objects.create(
        name="DAMA", description="Dimensions of Data Quality from DAMA (2020)"
    )

    # Create Dimensions
    dimensions = [
        {
            "name": "Accuracy",
            "description": "The degree of closeness of data values to real values.",
        },
        {
            "name": "Availability",
            "description": "The degree to which data can be consulted or retrieved by data consumers or a process.",
        },
        {
            "name": "Clarity",
            "description": "The ease with which data consumers can understand the metadata.",
        },
        {
            "name": "Completeness",
            "description": "The degree to which all required data values are present.",
        },
        {
            "name": "Consistency",
            "description": "The degree to which data values of two sets of attributes 1) within a record, 2) within a data file, 3) between data files, 4) within a record at different points in time, comply with a rule.",
        },
        {
            "name": "Currency",
            "description": "The degree to which data values are up to date.",
        },
        {
            "name": "Punctuality",
            "description": "The degree to which the period between the actual and target point of time of availability of a dataset is appropriate.",
        },
        {
            "name": "Timeliness",
            "description": "The degree to which the period between the time of creation of the real value and the time that the dataset is available is appropriate.",
        },
        {
            "name": "Traceability",
            "description": "The degree to which data lineage is available.",
        },
        {
            "name": "Uniqueness",
            "description": "The degree to which records occur only once in a data file.",
        },
        {
            "name": "Validity",
            "description": "The degree to which data values comply with rules.",
        },
    ]

    for dimension in dimensions:
        Dimension.objects.create(
            group=group, name=dimension["name"], description=dimension["description"]
        )


def rollback_dimension_group_and_dimensions(apps, schema_editor):
    DimensionGroup = apps.get_model("profiling", "DimensionGroup")
    Dimension = apps.get_model("profiling", "Dimension")

    # Get the group to delete dimensions and the group itself
    try:
        group = DimensionGroup.objects.get(name="DAMA")
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
        ("profiling", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            populate_dimension_group_and_dimensions,
            rollback_dimension_group_and_dimensions,
        ),
    ]
