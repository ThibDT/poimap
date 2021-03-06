# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-04 14:13
from __future__ import unicode_literals

import autoslug.fields
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0027_area_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=500)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from=b'name')),
                ('description', models.TextField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(dim=3, srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='area',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from=b'name'),
        ),
    ]
