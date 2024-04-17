# Generated by Django 3.2.25 on 2024-04-17 14:20

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20240416_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=5400)),
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(14, 20, 7, 34191)),
        ),
    ]
