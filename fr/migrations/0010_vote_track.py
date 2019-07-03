# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-23 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fr', '0009_delete_vote_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote_Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id_voter', models.CharField(max_length=100)),
                ('comment_id', models.CharField(max_length=100)),
                ('vote_type', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]