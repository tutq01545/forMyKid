# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-02 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=30)),
                ('calculation_mass', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InformationPerPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('from_to', models.CharField(blank=True, max_length=255)),
                ('quantity', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthAnalytic.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('birth_place', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='informationperperiod',
            name='kid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthAnalytic.Kid'),
        ),
    ]
