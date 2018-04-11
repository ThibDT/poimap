# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0014_graphedge'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphedge',
            name='routes',
            field=models.ManyToManyField(to='transportation.Route'),
        ),
    ]