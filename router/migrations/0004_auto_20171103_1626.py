# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0003_auto_20171103_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='loopback',
            field=models.GenericIPAddressField(),
        ),
    ]