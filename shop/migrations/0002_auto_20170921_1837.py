# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='shop.ProductCategory'),
        ),
    ]
