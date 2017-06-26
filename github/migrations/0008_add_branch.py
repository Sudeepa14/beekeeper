# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-26 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0007_require_pr_commit'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='branch',
            field=models.CharField(db_index=True, default='master', max_length=100),
            preserve_default=False,
        ),
    ]
