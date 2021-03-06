# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(blank=True, max_length=30)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
