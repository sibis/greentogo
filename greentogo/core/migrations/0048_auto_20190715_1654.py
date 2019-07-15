# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-07-15 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20190704_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtag',
            name='emailed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='preferred_delivery_time',
            field=models.CharField(choices=[('Anytime', 'Anytime'), ('8am', '8 am'), ('9am', '9 am'), ('10am', '10 am'), ('11am', '11 am'), ('12pm', '12 pm'), ('1pm', '1 pm'), ('2pm', '2 pm'), ('3pm', '3 pm'), ('4pm', '4 pm'), ('5pm', '5 pm'), ('6pm', '6 pm'), ('7pm', '7 pm'), ('8pm', '8 pm'), ('9pm', '9 pm')], default='Anytime', max_length=25),
        ),
    ]
