# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import dept.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_id', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('course_code', models.CharField(default=b'null', max_length=10)),
                ('course_name', models.CharField(default=b'null', max_length=50)),
                ('credits', models.IntegerField(default=0)),
                ('contact_hours', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=1, choices=[(2, b'Practical'), (1, b'Theory')])),
                ('b_tech', models.BooleanField(default=True)),
                ('idd', models.BooleanField(default=True)),
                ('m_tech', models.BooleanField(default=True)),
                ('ph_d', models.BooleanField(default=True)),
                ('dept', models.CharField(max_length=3)),
                ('course_offered_by', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_code', models.CharField(max_length=2, unique=True, serialize=False, verbose_name=b'Department Code', primary_key=True)),
                ('dept_name', models.CharField(max_length=50, null=True, verbose_name=b'Department Name')),
                ('contact1', models.IntegerField(validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact2', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('dept_heading', models.TextField(null=True, verbose_name=b'Department heading', blank=True)),
                ('about', models.TextField(default=b"This can't be empty")),
                ('b_tech', models.BooleanField(default=True, verbose_name=b'B.Tech')),
                ('idd', models.BooleanField(default=True, verbose_name=b'IDD')),
                ('m_tech', models.BooleanField(default=True, verbose_name=b'M.Tech')),
                ('ph_d', models.BooleanField(default=True, verbose_name=b'PhD')),
            ],
        ),
        migrations.CreateModel(
            name='FacultiesPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.ForeignKey(verbose_name=b'Department', to='dept.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(default=b'null', upload_to=dept.models.__get_path_faculty__)),
                ('designation', models.CharField(max_length=50, null=True, blank=True)),
                ('qualification', models.CharField(max_length=100, null=True, blank=True)),
                ('area_of_interest', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_off', models.IntegerField(blank=True, null=True, verbose_name=b'Contact office', validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_res', models.IntegerField(blank=True, null=True, verbose_name=b'Contact residence', validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_other', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('email_off', models.EmailField(max_length=254, unique=True, error_messages={b'invalid': b'Enter your Official Email-ID.'}, verbose_name=b'E-mail official', validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')])),
                ('email_other', models.EmailField(default=None, max_length=254, unique=True, null=True, blank=True)),
                ('status', models.CharField(max_length=10, null=True, blank=True)),
                ('faculty_id', models.CharField(max_length=100, unique=True, serialize=False, editable=False, primary_key=True)),
                ('dept', models.ForeignKey(verbose_name=b'Department', to='dept.Department')),
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
            name='HeadOfDepartments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.ForeignKey(to='dept.Department')),
                ('name', models.ForeignKey(to='dept.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Phd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('supervisor', models.CharField(max_length=50, null=True, blank=True)),
                ('co_supervisor', models.CharField(max_length=50, null=True, blank=True)),
                ('dept', models.ForeignKey(verbose_name=b'Department', to='dept.Department')),
            ],
        ),
        migrations.CreateModel(
            name='PhdResearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('supervisor', models.CharField(max_length=50, null=True, blank=True)),
                ('topic', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(verbose_name=b'Department', to='dept.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('post_hold_by', models.CharField(max_length=5, choices=[(b'3', b'Staff'), (b'4', b'Others'), (b'1', b'Faculty'), (b'2', b'Student')])),
                ('group', models.ForeignKey(to='dept.Groups')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=30, null=True, blank=True)),
                ('project', models.CharField(max_length=100)),
                ('sponsor', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0.0)),
                ('units', models.CharField(max_length=15, choices=[(b'Lakhs', b'Lakhs'), (b'Thousand', b'Thousand'), (b'Millions', b'Millions'), (b'Crores', b'Crores')])),
                ('investigator', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(to='dept.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('dept', models.ForeignKey(verbose_name=b'Department', to='dept.Department')),
            ],
        ),
        migrations.CreateModel(
            name='StaffsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_id', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')])),
                ('post', models.ForeignKey(to='dept.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')])),
                ('name', models.CharField(max_length=50)),
                ('year_of_admission', models.PositiveSmallIntegerField(default=0, editable=False)),
                ('degree', models.IntegerField(default=1, choices=[(3, b'M.Tech'), (1, b'B.Tech'), (2, b'IDD')])),
                ('email', models.EmailField(max_length=254, unique=True, error_messages={b'invalid': b'Enter your Official Email-ID.'}, validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')])),
                ('dept', models.ForeignKey(verbose_name=b'Department', to='dept.Department')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')])),
                ('post', models.ForeignKey(to='dept.Post')),
            ],
        ),
        migrations.AddField(
            model_name='facultiespost',
            name='faculty',
            field=models.ForeignKey(to='dept.Faculty'),
        ),
        migrations.AddField(
            model_name='facultiespost',
            name='post',
            field=models.ForeignKey(to='dept.Post'),
        ),
    ]
