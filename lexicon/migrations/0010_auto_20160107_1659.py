# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0009_auto_20160107_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_example',
            field=models.TextField(blank=True, null=True),
        ),
    ]
