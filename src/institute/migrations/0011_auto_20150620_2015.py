# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0010_auto_20150608_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultiesPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short', models.CharField(unique=True, max_length=10)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('post_hold_by', models.CharField(max_length=5, choices=[(b'3', b'Staff'), (b'4', b'Others'), (b'1', b'Faculty'), (b'2', b'Student')])),
                ('group', models.ForeignKey(to='institute.Groups')),
            ],
        ),
        migrations.CreateModel(
            name='StaffsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_id', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')])),
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
        migrations.RemoveField(
            model_name='department',
            name='hod_email',
        ),
        migrations.RemoveField(
            model_name='department',
            name='hod_name',
        ),
        migrations.RemoveField(
            model_name='phdresearch',
            name='sv_desgination',
        ),
        migrations.AddField(
            model_name='adminofficial',
            name='rank_name',
            field=models.CharField(default=datetime.datetime(2015, 6, 20, 20, 15, 6, 555155, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='headofdepartments',
            name='department',
            field=models.ForeignKey(default=datetime.datetime(2015, 6, 20, 20, 15, 25, 468192, tzinfo=utc), to='institute.Department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='headofdepartments',
            name='name',
            field=models.ForeignKey(to='institute.Faculty'),
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.AddField(
            model_name='facultiespost',
            name='dept',
            field=models.ForeignKey(to='institute.Department'),
        ),
        migrations.AddField(
            model_name='facultiespost',
            name='faculty',
            field=models.ForeignKey(to='institute.Faculty'),
        ),
        migrations.AddField(
            model_name='facultiespost',
            name='post',
            field=models.ForeignKey(to='institute.Post'),
        ),
    ]
