# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0011_auto_20170302_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='scanned',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
