# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0012_auto_20180401_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
