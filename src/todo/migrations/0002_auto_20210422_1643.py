# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-04-22 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
