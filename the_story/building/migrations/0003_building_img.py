# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_auto_20170708_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='img',
            field=models.ImageField(default=None, upload_to='building/'),
            preserve_default=False,
        ),
    ]
