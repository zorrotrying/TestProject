# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-26 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0010_auto_20170726_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_cdap',
            old_name='author',
            new_name='user',
        ),
    ]