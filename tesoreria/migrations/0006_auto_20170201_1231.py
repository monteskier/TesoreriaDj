# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesoreria', '0005_auto_20170201_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitat',
            name='nom',
            field=models.CharField(max_length=200),
        ),
    ]
