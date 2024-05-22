# Generated by Django 4.2.13 on 2024-05-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis_ontology", "0057_expression_volume"),
    ]

    operations = [
        migrations.AddField(
            model_name="worktype",
            name="icon_id",
            field=models.CharField(
                blank=True,
                default="",
                max_length=50,
                verbose_name="Icon-Kennzeichnung",
            ),
        ),
    ]
