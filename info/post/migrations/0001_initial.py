# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-21 18:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=1000)),
                ('cantity', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, null=True, upload_to=post.models.upload_location)),
                ('price', models.CharField(max_length=15)),
                ('delivery_time', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
