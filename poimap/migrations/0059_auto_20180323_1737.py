# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0058_poirating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poirating',
            name='score',
            field=models.FloatField(),
        ),
    ]