# Generated by Django 3.2.25 on 2024-04-24 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.DurationField(blank=True, help_text='Enter duration in the format HH:MM:SS', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(13, 6, 46, 872153)),
        ),
    ]