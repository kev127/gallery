# Generated by Django 3.1.3 on 2020-11-15 10:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20201115_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='gallery/'),
        ),
    ]
