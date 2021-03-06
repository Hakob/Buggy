# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 09:58
from __future__ import unicode_literals

import buggy.enums
import buggy.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('bug', 'order'),
            },
        ),
        migrations.CreateModel(
            name='AddAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=255, upload_to=buggy.models.attachment_upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('state', enumfields.fields.EnumField(enum=buggy.enums.State, max_length=25)),
                ('priority', enumfields.fields.EnumIntegerField(enum=buggy.enums.Priority)),
                ('fulltext', models.TextField()),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PresetFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('action', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='buggy.Action')),
                ('comment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SetAssignment',
            fields=[
                ('action', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='buggy.Action')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SetCategory',
            fields=[
                ('action', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='buggy.Action')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buggy.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SetPriority',
            fields=[
                ('action', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='buggy.Action')),
                ('priority', enumfields.fields.EnumIntegerField(enum=buggy.enums.Priority)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SetState',
            fields=[
                ('action', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='buggy.Action')),
                ('state', enumfields.fields.EnumField(enum=buggy.enums.State, max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SetTitle',
            fields=[
                ('action', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='buggy.Action')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bug',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buggy.Category'),
        ),
        migrations.AddField(
            model_name='bug',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addattachment',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='buggy.Action'),
        ),
        migrations.AddField(
            model_name='action',
            name='bug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='buggy.Bug'),
        ),
        migrations.AddField(
            model_name='action',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='presetfilter',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='action',
            unique_together=set([('bug', 'order')]),
        ),
    ]
