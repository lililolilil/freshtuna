# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='BoardNm',
            new_name='boardNm',
        ),
        migrations.AddField(
            model_name='board',
            name='title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
