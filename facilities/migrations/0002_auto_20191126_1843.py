# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-26 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayoff',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
