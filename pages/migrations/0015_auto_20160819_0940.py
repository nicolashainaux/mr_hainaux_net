# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20160803_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='html_name',
            field=models.CharField(default='unset', max_length=100),
        ),
        migrations.AddField(
            model_name='footercategory',
            name='html_name',
            field=models.CharField(default='unset', max_length=100),
        ),
        migrations.AddField(
            model_name='news',
            name='html_title',
            field=models.CharField(default='unset', max_length=100),
        ),
        migrations.AddField(
            model_name='theme',
            name='html_name',
            field=models.CharField(default='unset', max_length=100),
        ),
        migrations.AddField(
            model_name='tile',
            name='html_name',
            field=models.CharField(default='unset', max_length=100),
        ),
    ]
