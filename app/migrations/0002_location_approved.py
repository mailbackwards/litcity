# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
