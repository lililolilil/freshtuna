# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171124_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='boardcd',
        ),
    ]