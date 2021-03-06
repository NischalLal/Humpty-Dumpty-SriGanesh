# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_from_me', models.TextField()),
                ('subject', models.CharField(max_length=33)),
                ('message_from_user', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('image', models.ImageField(default=None, upload_to='myblog/image/project')),
                ('detail', models.TextField()),
                ('created_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=10)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Social Sites',
            },
        ),
    ]
