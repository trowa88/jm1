# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='title',
            new_name='name',
        ),
    ]
