# Generated by Django 4.0 on 2023-07-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='concept_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
