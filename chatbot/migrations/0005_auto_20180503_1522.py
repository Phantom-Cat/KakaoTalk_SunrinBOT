# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_auto_20180503_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_key',
            name='key',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
