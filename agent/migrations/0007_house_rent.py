# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-25 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0006_auto_20190725_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='rent',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]