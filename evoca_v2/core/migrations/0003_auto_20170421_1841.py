# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170421_1825'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dimensions',
            new_name='Dimension',
        ),
    ]
