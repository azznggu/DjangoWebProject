# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
