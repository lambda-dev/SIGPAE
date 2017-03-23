# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0027_auto_20170315_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='document',
            name='nombre',
            field=models.CharField(max_length=128, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='document',
            name='telefono',
            field=models.CharField(max_length=30, verbose_name='Teléfono'),
        ),
    ]
