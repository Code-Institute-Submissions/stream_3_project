# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productimage_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='featured',
        ),
    ]
