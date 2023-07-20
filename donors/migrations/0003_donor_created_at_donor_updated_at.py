# Generated by Django 4.0 on 2023-07-19 23:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0002_donor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
