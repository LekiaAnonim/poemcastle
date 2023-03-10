# Generated by Django 4.1.7 on 2023-03-10 22:16

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem_castle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='poem',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
