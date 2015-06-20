# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0012_auto_20150613_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultiesPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.ForeignKey(to='institute.Department')),
                ('faculty', models.ForeignKey(to='institute.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short', models.CharField(unique=True, max_length=10)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('post_hold_by', models.CharField(max_length=1, choices=[(3, b'Staff'), (4, b'Others'), (2, b'Student'), (1, b'Faculty')])),
                ('group', models.ForeignKey(to='institute.Groups')),
            ],
        ),
        migrations.CreateModel(
            name='StaffsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')])),
                ('post', models.ForeignKey(to='institute.Post')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')])),
                ('post', models.ForeignKey(to='institute.Post')),
            ],
        ),
        migrations.DeleteModel(
            name='Committee',
        ),
        migrations.RemoveField(
            model_name='history',
            name='rank_id',
        ),
        migrations.DeleteModel(
            name='HostelAdmin',
        ),
        migrations.DeleteModel(
            name='Wmes',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.AddField(
            model_name='facultiespost',
            name='post',
            field=models.ForeignKey(to='institute.Post'),
        ),
    ]
