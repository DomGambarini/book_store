# Generated by Django 3.2.25 on 2024-04-25 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_alter_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(10, 15, 23, 962728), help_text='Enter time in the format of the 24 clock'),
        ),
    ]
