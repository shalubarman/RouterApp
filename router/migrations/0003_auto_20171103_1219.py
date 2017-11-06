# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0002_auto_20171103_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='hostname',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='router',
            name='loopback',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterUniqueTogether(
            name='router',
            unique_together=set([('hostname', 'loopback')]),
        ),
    ]
