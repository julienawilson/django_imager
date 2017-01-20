# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='imager_profile.ImagerProfile'),
        ),
        migrations.AlterField(
            model_name='image',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='imager_profile.ImagerProfile'),
        ),
    ]
