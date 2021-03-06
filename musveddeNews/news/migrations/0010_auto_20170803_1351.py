# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170803_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_level',
        ),
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='super_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='super_children', to='news.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='news.Category'),
        ),
    ]
