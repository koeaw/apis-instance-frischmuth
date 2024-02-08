# Generated by Django 4.2.10 on 2024-02-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis_ontology", "0034_alter_expression_publication_date_iso"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expression",
            name="relevant_pages",
            field=models.CharField(
                blank=True,
                help_text='Eingabe muss im Format "X-Y" erfolgen, z.B. 5-12',
                null=True,
                verbose_name="Forschungsrelevante Seiten",
            ),
        ),
    ]
