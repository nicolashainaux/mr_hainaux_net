# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20160730_0648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thumbnail',
            new_name='Tile',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='unset', max_length=100),
        ),
    ]
