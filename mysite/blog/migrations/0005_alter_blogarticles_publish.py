# Generated by Django 4.2.9 on 2024-01-25 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogarticles_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 25, 7, 35, 19, 329158, tzinfo=datetime.timezone.utc)),
        ),
    ]
