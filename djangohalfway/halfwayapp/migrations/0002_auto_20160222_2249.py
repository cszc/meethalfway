# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('halfwayapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='starting_location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='halfwayapp.Address'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='transit_mode',
            field=models.CharField(max_length=64),
        ),
    ]
