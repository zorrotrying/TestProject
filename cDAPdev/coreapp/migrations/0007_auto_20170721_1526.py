# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-21 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0006_auto_20170721_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_cdap',
            name='type',
            field=models.CharField(choices=[('Python', 'python'), ('R', 'r'), ('Knime', 'knime'), ('Spotfire', 'spotfire'), ('Excel', 'excel')], max_length=32),
        ),
    ]
