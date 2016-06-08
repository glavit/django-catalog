# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20160606_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=350, verbose_name='Name')),
                ('key', models.SlugField(unique=True, verbose_name='Key')),
                ('kind', models.CharField(choices=[(b'string', 'string'), (b'int', 'Integer'), (b'bool', 'Bool'), (b'float', 'Float')], max_length=10, verbose_name='Kind')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('value', models.CharField(max_length=4096, verbose_name='Value')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.FeatureKey', verbose_name='Feature Key')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_features', to='catalog.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Feature Product',
                'verbose_name_plural': 'Feature Products',
            },
        ),
        migrations.CreateModel(
            name='GroupsFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Groups Feature',
                'verbose_name_plural': 'Groups Features',
            },
        ),
        migrations.RemoveField(
            model_name='features',
            name='group',
        ),
        migrations.RemoveField(
            model_name='featuresproduct',
            name='features',
        ),
        migrations.RemoveField(
            model_name='featuresproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='Features',
        ),
        migrations.DeleteModel(
            name='FeaturesProduct',
        ),
        migrations.DeleteModel(
            name='GroupsFeatures',
        ),
        migrations.AddField(
            model_name='featurekey',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_features', to='catalog.GroupsFeature', verbose_name='Group'),
        ),
    ]