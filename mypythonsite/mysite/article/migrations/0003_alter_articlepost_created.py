# Generated by Django 4.2.9 on 2024-01-23 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articlepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 3, 37, 39, 501240, tzinfo=datetime.timezone.utc)),
        ),
    ]
