# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 15:54
from __future__ import unicode_literals

from django.db import migrations
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0031_auto_20170605_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poitype',
            name='icon',
            field=fontawesome.fields.IconField(blank=True, max_length=60),
        ),
    ]