# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 03:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20170427_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='channel',
            name='uniqueID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, serialize=False),
        ),
        migrations.AddField(
            model_name='membership',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Channel'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='channel',
            name='members',
            field=models.ManyToManyField(related_name='channel_members', through='core.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
