# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20160725_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='CategoryContent',
        ),
    ]
