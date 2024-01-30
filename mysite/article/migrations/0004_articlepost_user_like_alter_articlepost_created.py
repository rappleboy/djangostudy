# Generated by Django 4.2.9 on 2024-01-24 14:13

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_alter_articlepost_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='user_like',
            field=models.ManyToManyField(blank=True, related_name='article_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 14, 13, 4, 717420, tzinfo=datetime.timezone.utc)),
        ),
    ]