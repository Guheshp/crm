# Generated by Django 5.0.1 on 2024-01-25 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_remove_receipe_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
