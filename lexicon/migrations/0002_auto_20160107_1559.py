# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_definition',
            field=models.TextField(default='n/a'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_example',
            field=models.TextField(default=None),
        ),
    ]
