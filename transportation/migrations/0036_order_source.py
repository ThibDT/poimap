# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-17 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0035_auto_20180716_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='source',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]