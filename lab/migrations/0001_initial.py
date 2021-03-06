# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=32)),
                ('date_expiration', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GeneAnalyte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('institution', models.CharField(blank=True, max_length=200, null=True)),
                ('abbreviation', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('fax', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=16)),
                ('data_sharing', models.BooleanField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('gtr_lab_id', models.PositiveIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.Country')),
            ],
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('conditions', models.ManyToManyField(to='lab.Condition')),
                ('gene_analytes', models.ManyToManyField(to='lab.GeneAnalyte')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=64)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('fax', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_joined', models.DateField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='labtest',
            name='methods',
            field=models.ManyToManyField(to='lab.Method'),
        ),
        migrations.AddField(
            model_name='lab',
            name='services',
            field=models.ManyToManyField(to='lab.Service'),
        ),
        migrations.AddField(
            model_name='certification',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Lab'),
        ),
    ]
