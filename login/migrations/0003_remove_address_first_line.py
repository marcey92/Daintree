# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_address_first_line'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='first_line',
        ),
    ]