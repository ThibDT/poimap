# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-14 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0027_auto_20180611_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transportation.Service'),
            preserve_default=False,
        ),
    ]
