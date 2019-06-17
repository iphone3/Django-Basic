# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-17 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='g_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='goods',
            name='g_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
