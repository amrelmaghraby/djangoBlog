# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170829_1324'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='posts',
        ),
    ]