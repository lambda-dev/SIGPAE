# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0017_auto_20170316_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencia',
            name='editorial',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='referencia',
            name='titulo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
