# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 12:50
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20160204_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon_symbol',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='icon_symbol/%Y/%m/%d'),
        ),
    ]
