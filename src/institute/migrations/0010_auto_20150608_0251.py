# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import institute.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0009_auto_20150604_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin_in_course', models.CharField(max_length=100, blank=True)),
                ('title', models.CharField(max_length=300)),
                ('adm_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_admdoc__)),
            ],
        ),
        migrations.CreateModel(
            name='CerdHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('desription', models.TextField()),
                ('Address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CerdPeople',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('desig', models.CharField(max_length=100)),
                ('profie_info', models.FileField(default=b'null', upload_to=institute.models.__get_path_cerd__)),
            ],
        ),
        migrations.CreateModel(
            name='Convo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('letter', models.FileField(default=b'null', upload_to=institute.models.__get_path_convo__)),
                ('Form', models.FileField(default=b'null', upload_to=institute.models.__get_path_convo__)),
                ('schedule', models.FileField(default=b'null', upload_to=institute.models.__get_path_convo__)),
                ('upload_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fee_from_year', models.CharField(max_length=100)),
                ('fee_for', models.CharField(max_length=100)),
                ('fee_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_feedoc__)),
            ],
        ),
        migrations.CreateModel(
            name='NewEntrants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('ne_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_newent__)),
            ],
        ),
        migrations.CreateModel(
            name='Ordinance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordinance_type', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('ord_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_orddoc__)),
            ],
        ),
        migrations.CreateModel(
            name='Phd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('supervisor', models.CharField(max_length=50, null=True, blank=True)),
                ('co_supervisor', models.CharField(max_length=50, null=True, blank=True)),
                ('dept', models.ForeignKey(to='institute.Department')),
            ],
        ),
        migrations.CreateModel(
            name='PhdResearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('supervisor', models.CharField(max_length=50, null=True, blank=True)),
                ('sv_desgination', models.CharField(max_length=50, null=True, blank=True)),
                ('topic', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(to='institute.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ScholarShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('scolar_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_schdoc__)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfAcademicProgrammes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('adm_through', models.CharField(max_length=10)),
                ('no_of_progs', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='id',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_id',
            field=models.CharField(max_length=100, unique=True, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=20, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')]),
        ),
    ]
