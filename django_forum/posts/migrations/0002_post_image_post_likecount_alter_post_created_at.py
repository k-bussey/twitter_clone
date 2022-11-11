# Generated by Django 4.1.3 on 2022-11-11 21:45

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='likecount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Like'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created DateTime'),
        ),
    ]
