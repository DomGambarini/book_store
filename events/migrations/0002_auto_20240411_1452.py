from datetime import time
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_datetime',
        ),
        migrations.AddField(
            model_name='event',
            name='date_field',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time_field',
            field=models.TimeField(default=time(hour=0, minute=0)),
            preserve_default=False,
        ),
    ]
