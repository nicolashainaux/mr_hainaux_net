# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='unset', max_length=100),
        ),
    ]
