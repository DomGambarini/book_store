# Generated by Django 3.2.25 on 2024-04-17 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20240417_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(14, 21, 56, 439283)),
        ),
    ]