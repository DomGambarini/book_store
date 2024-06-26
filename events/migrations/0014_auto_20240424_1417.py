# Generated by Django 3.2.25 on 2024-04-24 14:17

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Enter date in the format YYYY:MM:DD'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(14, 17, 11, 794836), help_text='Enter time in the format of the 24 clock'),
        ),
    ]
