# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20160204_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='icon_bookmark',
            field=models.ImageField(blank=True, height_field='32', null=True, upload_to='icon_bookmark/%Y/%m/%d', width_field='32'),
        ),
    ]
