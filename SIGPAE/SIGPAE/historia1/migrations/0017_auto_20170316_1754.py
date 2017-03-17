# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 17:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0016_auto_20170303_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, verbose_name='Código de la materia')),
                ('materia', models.CharField(blank=True, max_length=255, verbose_name='Denominación')),
                ('h_teoria', models.PositiveIntegerField(blank=True, null=True, verbose_name='Horas de Teoría')),
                ('h_prac', models.PositiveIntegerField(blank=True, null=True, verbose_name='Horas de Práctica')),
                ('h_lab', models.PositiveIntegerField(blank=True, null=True, verbose_name='Horas de Laboratorio')),
                ('fecha_vigtrim', models.CharField(choices=[('AB', 'Abril - Julio'), ('EM', 'Enero - Marzo'), ('SD', 'Septiembre - Diciembre'), ('NN', 'Ninguno')], default='NN', max_length=2, verbose_name='Trimestre')),
                ('fecha_vigano', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2017), django.core.validators.MinValueValidator(1969)], verbose_name='Año')),
                ('obj_g', models.TextField(blank=True, verbose_name='Objetivos Generales')),
                ('obj_e', models.TextField(blank=True, verbose_name='Objetivos Específicos')),
                ('contenidos', models.TextField(blank=True, verbose_name='Contenidos')),
                ('estrategias', models.TextField(blank=True, verbose_name='Estrategias Metodológicas')),
                ('estrat_eval', models.TextField(blank=True, verbose_name='Estrategias de Evaluación')),
                ('fuentes', models.TextField(blank=True, verbose_name='Fuentes de Información Recomendadas')),
                ('cronograma', models.TextField(blank=True, verbose_name='Cronograma')),
                ('sinoptico', models.TextField(blank=True, verbose_name='Contenidos Sińópticos')),
            ],
        ),
        migrations.CreateModel(
            name='Rafael',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('editorial', models.CharField(max_length=255)),
                ('edicion', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('editorial', models.CharField(max_length=255)),
                ('edicion', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='asignatura',
            field=models.CharField(blank=True, max_length=255, verbose_name='Denominación'),
        ),
        migrations.AlterField(
            model_name='document',
            name='bibliografias',
            field=models.TextField(blank=True, verbose_name='Fuentes de Información Recomendadas'),
        ),
        migrations.AlterField(
            model_name='document',
            name='codigo',
            field=models.CharField(blank=True, max_length=10, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='document',
            name='creditos',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(16), django.core.validators.MinValueValidator(0)], verbose_name='Unidades Créditos'),
        ),
        migrations.AlterField(
            model_name='document',
            name='trimestre',
            field=models.CharField(choices=[('AB', 'Abril - Julio'), ('EM', 'Enero - Marzo'), ('SD', 'Septiembre - Diciembre'), ('NN', 'Ninguno')], default='NN', max_length=2),
        ),
        migrations.AlterField(
            model_name='document',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2017), django.core.validators.MinValueValidator(1969)], verbose_name='Año'),
        ),
        migrations.AddField(
            model_name='referencia',
            name='document',
            field=models.ManyToManyField(to='historia1.Document'),
        ),
        migrations.AddField(
            model_name='rafael',
            name='document',
            field=models.ManyToManyField(to='historia1.Document'),
        ),
        migrations.AddField(
            model_name='autores',
            name='referencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historia1.Referencia'),
        ),
    ]