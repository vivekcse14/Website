# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import institute.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminOfficial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank_id', models.IntegerField()),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('qualification', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_off', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_res', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_other', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('email_off', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('email_other', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('fax', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardOfGovernor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=100, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('rank', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comm_id', models.IntegerField()),
                ('comm_for', models.CharField(max_length=100, null=True, blank=True)),
                ('notif_no', models.CharField(max_length=100, null=True, blank=True)),
                ('dated', models.CharField(max_length=100, null=True, blank=True)),
                ('comm_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_committees__)),
                ('comm_img', models.ImageField(default=b'null', upload_to=institute.models.__get_path_committees__)),
            ],
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('comm_id', models.IntegerField(serialize=False, primary_key=True)),
                ('comm_related_to', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('s_no', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('course_id', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
                ('contact_hours', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('b_tech', models.IntegerField(default=0)),
                ('idd', models.IntegerField(default=0)),
                ('m_tech', models.IntegerField(default=0)),
                ('ph_d', models.IntegerField(default=0)),
                ('dept', models.CharField(max_length=3)),
                ('course_offered_by', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_code', models.CharField(max_length=2, unique=True, serialize=False, primary_key=True)),
                ('dept_name', models.CharField(max_length=50, null=True)),
                ('hod_name', models.CharField(max_length=50)),
                ('hod_email', models.EmailField(max_length=254)),
                ('contact1', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact2', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=100, null=True, blank=True)),
                ('event_dt', models.CharField(max_length=100, null=True, blank=True)),
                ('event_venue', models.CharField(max_length=100, null=True, blank=True)),
                ('event_desc', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(default=b'null', upload_to=institute.models.__get_path_faculty__)),
                ('designation', models.CharField(max_length=20, null=True, blank=True)),
                ('qualification', models.CharField(max_length=100, null=True, blank=True)),
                ('area_of_interest', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_off', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_res', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_other', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('email_off', models.EmailField(unique=True, max_length=254)),
                ('email_other', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('status', models.CharField(max_length=10, null=True, blank=True)),
                ('faculty_id', models.CharField(unique=True, max_length=100)),
                ('dept', models.ForeignKey(to='institute.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('gallery_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('gallery_of', models.CharField(max_length=50, null=True, blank=True)),
                ('gallery_title', models.CharField(max_length=50, null=True, blank=True)),
                ('gallery_desc', models.CharField(max_length=100, null=True, blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('tenure_start', models.CharField(max_length=100, null=True, blank=True)),
                ('tenure_end', models.CharField(max_length=100, null=True, blank=True)),
                ('photo', models.ImageField(upload_to=institute.models.__get_path_directors__)),
            ],
        ),
        migrations.CreateModel(
            name='HostelAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostel', models.CharField(max_length=100, null=True, blank=True)),
                ('admin_war', models.CharField(max_length=100, null=True, blank=True)),
                ('war1', models.CharField(max_length=100, null=True, blank=True)),
                ('war2', models.CharField(max_length=100, null=True, blank=True)),
                ('email_admin', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('email_war1', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('email_war2', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('img_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('img_caption', models.CharField(max_length=50, null=True, blank=True)),
                ('img', models.ImageField(default=b'null', upload_to=institute.models.__get_path_gallery__)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('gallery_id', models.ForeignKey(to='institute.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notif_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('priority', models.IntegerField(default=3, choices=[(2, b'Normal'), (1, b'High'), (3, b'Low')])),
                ('quality', models.CharField(default=b'old', max_length=3)),
                ('notif_of', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100, null=True, blank=True)),
                ('notif_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_notif__)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RankList',
            fields=[
                ('rank_id', models.IntegerField(serialize=False, primary_key=True)),
                ('rank_name', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeminarsConf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100, null=True, blank=True)),
                ('doc', models.FileField(upload_to=institute.models.__get_path_seminars__)),
                ('date', models.CharField(max_length=20, null=True, blank=True)),
                ('time', models.CharField(max_length=10, null=True, blank=True)),
                ('venue', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('dept', models.ForeignKey(to='institute.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(b'^[0-9 a-z A-Z]*$', b'Only Alphanumeric values are allowed')])),
                ('name', models.CharField(max_length=50)),
                ('year_of_admission', models.IntegerField()),
                ('degree', models.CharField(max_length=10)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('dept', models.ForeignKey(to='institute.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tender_id', models.CharField(max_length=100, null=True, blank=True)),
                ('dept', models.CharField(max_length=100, null=True, blank=True)),
                ('posting_dt', models.CharField(max_length=100, null=True, blank=True)),
                ('closing_dt', models.CharField(max_length=100, null=True, blank=True)),
                ('desc', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TenderDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tender_id', models.CharField(max_length=100, null=True, blank=True)),
                ('tender_name', models.CharField(max_length=100, null=True, blank=True)),
                ('tender_doc', models.FileField(upload_to=institute.models.__get_path_tenders__)),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='rank_id',
            field=models.ForeignKey(to='institute.RankList'),
        ),
    ]
