# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20160730_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'news',
            },
        ),
    ]
