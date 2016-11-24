# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 12:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('Distrito', models.CharField(max_length=200)),
                ('Concelho', models.CharField(max_length=200)),
                ('Freguesia', models.CharField(max_length=200)),
                ('Nome', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]