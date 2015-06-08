# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import institute.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0008_auto_20150605_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sem_name', models.CharField(max_length=100, blank=True)),
                ('sem_type', models.CharField(max_length=4)),
                ('registration_date', models.DateField()),
                ('calendar_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_calendar__)),
                ('sem_comnc_date', models.DateField()),
                ('sem_reg_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Circulars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('ref_no', models.CharField(max_length=100, blank=True)),
                ('date', models.DateField(null=True)),
                ('cir_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_cir__)),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfDepartments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=100, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_of', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('descr', models.TextField(blank=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RightToInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_reg', models.CharField(max_length=300, null=True, blank=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('rti_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_rti__)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('designation', models.CharField(max_length=100, null=True, blank=True)),
                ('contact', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
            ],
        ),
        migrations.CreateModel(
            name='Wmes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desig', models.CharField(max_length=100, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('linked_in', models.CharField(unique=True, max_length=200, blank=True)),
                ('dept', models.CharField(max_length=100)),
                ('mem_type', models.CharField(max_length=100)),
                ('prof_pic', models.FileField(default=b'null', upload_to=institute.models.__get_path_wmes__)),
            ],
        ),
        migrations.AddField(
            model_name='adminofficial',
            name='rank_area',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.IntegerField(default=1, choices=[(3, b'M.Tech'), (1, b'B.Tech'), (2, b'IDD')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_of_admission',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
