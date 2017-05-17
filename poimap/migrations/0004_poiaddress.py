# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 21:13
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0003_auto_20170327_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='POIAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('zipcode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=300)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]