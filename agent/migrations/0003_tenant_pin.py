# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-24 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_auto_20190724_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='pin',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]
