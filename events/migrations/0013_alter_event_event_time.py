# Generated by Django 3.2.25 on 2024-04-24 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20240424_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(13, 8, 31, 126138)),
        ),
    ]
