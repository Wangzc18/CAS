# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='work_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
