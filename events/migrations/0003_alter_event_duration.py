# Generated by Django 3.2.25 on 2024-04-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20240411_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.CharField(max_length=50),
        ),
    ]
