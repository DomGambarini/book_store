# Generated by Django 3.2.25 on 2024-04-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_alter_team_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='bio',
            field=models.TextField(max_length=1000),
        ),
    ]