# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-10-27 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20190925_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_checkout', models.DateField(auto_now_add=True)),
                ('count', models.IntegerField()),
                ('checked_out', models.BooleanField(default=False)),
                ('checked_in', models.BooleanField(default=False)),
                ('item_type', models.CharField(choices=[('CUP', 'Cup'), ('BOX', 'Box')], default='BOX', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('corporate_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CorporateCode')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subscription')),
            ],
        ),
    ]
