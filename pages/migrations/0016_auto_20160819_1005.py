# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20160819_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]