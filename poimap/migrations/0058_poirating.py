# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poimap', '0057_auto_20180322_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='POIRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True)),
                ('poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='poimap.POI')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
