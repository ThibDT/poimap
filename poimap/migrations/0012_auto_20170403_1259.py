# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0011_auto_20170403_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
