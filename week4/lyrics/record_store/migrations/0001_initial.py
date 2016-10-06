# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('lyrics', models.TextField()),
                ('release_year', models.IntegerField()),
            ],
        ),
    ]
