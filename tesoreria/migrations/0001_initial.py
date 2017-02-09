# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codi', models.IntegerField(max_length=10)),
                ('nom', models.CharField(max_length=100)),
                ('iban', models.CharField(max_length=24)),
                ('email', models.CharField(max_length=200, null=True)),
                ('telefon', models.DecimalField(decimal_places=0, max_digits=9, null=True)),
                ('saldo_inicial', models.DecimalField(decimal_places=2, max_digits=9)),
                ('saldo_ajuntament', models.DecimalField(decimal_places=2, max_digits=9)),
                ('saldo_final', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Moviments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_mov', models.DateTimeField(verbose_name='Data del moviment')),
                ('operacio', models.CharField(max_length=500)),
                ('accio', models.CharField(choices=[('Entrada', 'Entrada'), ('Sortida', 'Sortida'), ('Traspas', 'Traspas')], default='Entrada', max_length=200)),
                ('codiEnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codiEnt', to='tesoreria.Entitat')),
            ],
        ),
    ]
