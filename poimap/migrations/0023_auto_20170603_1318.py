# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-03 11:18
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0022_auto_20170603_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(dim=3, geography=True, srid=4326),
        ),
    ]
