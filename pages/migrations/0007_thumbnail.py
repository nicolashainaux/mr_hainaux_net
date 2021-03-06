# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Theme')),
            ],
        ),
    ]
