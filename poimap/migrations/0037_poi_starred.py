# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-05 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0036_auto_20170730_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='starred',
            field=models.BooleanField(default=False),
        ),
    ]
