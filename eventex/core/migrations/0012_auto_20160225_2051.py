# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20160225_1302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['start'], 'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
    ]
