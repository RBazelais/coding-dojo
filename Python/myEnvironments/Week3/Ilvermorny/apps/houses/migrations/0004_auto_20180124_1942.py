# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cult',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peeps', to='houses.House'),
        ),
    ]
