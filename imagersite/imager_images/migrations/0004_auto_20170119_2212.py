# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_auto_20170119_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ManyToManyField(related_name='albums', to='imager_images.Image'),
        ),
    ]
