# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 15:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0048_auto_20180208_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poi',
            options={'ordering': ['distance', 'name'], 'verbose_name': 'POI', 'verbose_name_plural': 'POI'},
        ),
    ]
