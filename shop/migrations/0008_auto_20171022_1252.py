# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20171022_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=b'', max_digits=15),
        ),
    ]
