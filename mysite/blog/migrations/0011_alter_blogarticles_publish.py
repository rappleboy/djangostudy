# Generated by Django 4.2.9 on 2024-01-27 06:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogarticles_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 6, 3, 38, 350877, tzinfo=datetime.timezone.utc)),
        ),
    ]