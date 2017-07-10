# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_build_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='result',
            field=models.IntegerField(choices=[(0, 'Pending'), (10, 'Fail'), (19, 'Non-critical Fail'), (20, 'Pass')], default=0),
        ),
    ]