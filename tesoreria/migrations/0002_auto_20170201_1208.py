# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesoreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitat',
            name='nom',
            field=models.CharField(max_length=100),
        ),
    ]
