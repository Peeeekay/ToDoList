# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-05 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=2),
            preserve_default=False,
        ),
    ]