# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-15 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20180703_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
