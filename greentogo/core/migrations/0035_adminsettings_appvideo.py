# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-20 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20180929_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminsettings',
            name='appVideo',
            field=models.FileField(blank=True, null=True, upload_to='video/'),
        ),
    ]