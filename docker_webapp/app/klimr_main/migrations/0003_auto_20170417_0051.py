# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klimr_main', '0002_queuerecord_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='reason',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='lesson',
            name='state',
            field=models.IntegerField(choices=[(0, 'Scheduled'), (1, 'On Time'), (2, 'Arrived'), (3, 'Cancelled')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='subgroup',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='klimr_main.Subgroup'),
            preserve_default=False,
        ),
    ]
