# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-17 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190617_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='score',
        ),
        migrations.AddField(
            model_name='student',
            name='english',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='math',
            field=models.IntegerField(default=0),
        ),
    ]
