# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albuns', '0003_auto_20171010_1111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Albuns',
            new_name='Album',
        ),
    ]