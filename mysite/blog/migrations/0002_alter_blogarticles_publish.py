# Generated by Django 4.2.9 on 2024-01-23 03:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 3, 36, 20, 256540, tzinfo=datetime.timezone.utc)),
        ),
    ]