# Generated by Django 3.2.25 on 2024-04-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/media/noimage.png', upload_to=''),
        ),
    ]
