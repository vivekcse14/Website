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
                ('rank_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('rank_area', models.CharField(max_length=100, blank=True)),
                ('qualification', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_off', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_res', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('contact_other', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('email_off', models.EmailField(null=True, validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')], error_messages={b'invalid': b'Enter your Official Email-ID.'}, max_length=254, blank=True, unique=True)),
                ('email_other', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('fax', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin_in_course', models.CharField(max_length=100, blank=True)),
                ('title', models.CharField(max_length=300)),
                ('adm_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_admdoc__, verbose_name=b'Admission document')),
            ],
        ),
        migrations.CreateModel(
            name='BoardOfGovernor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=100, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('rank', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('nominated_by', models.CharField(max_length=100)),
            ],
        ),
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
            name='CommDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comm_id', models.IntegerField()),
                ('comm_for', models.CharField(max_length=100, null=True, blank=True)),
                ('notif_no', models.CharField(max_length=100, null=True, verbose_name=b'Notification number', blank=True)),
                ('dated', models.CharField(max_length=100, null=True, blank=True)),
                ('comm_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_committees__)),
                ('comm_img', models.ImageField(default=b'null', upload_to=institute.models.__get_path_committees__)),
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
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=100, null=True, blank=True)),
                ('event_dt', models.CharField(max_length=100, null=True, verbose_name=b'Event date', blank=True)),
                ('event_venue', models.CharField(max_length=100, null=True, blank=True)),
                ('event_desc', models.CharField(max_length=100, null=True, verbose_name=b'Event description', blank=True)),
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
            name='NewEntrants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('ne_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_newent__)),
            ],
        ),
        migrations.CreateModel(
            name='NewsBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_of', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('descr', models.TextField(verbose_name=b'Description', blank=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notif_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('priority', models.IntegerField(default=3, choices=[(2, b'Normal'), (1, b'High'), (3, b'Low')])),
                ('quality', models.IntegerField(default=1, choices=[(1, b'new'), (0, b'old')])),
                ('notif_of', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100, null=True, blank=True)),
                ('notif_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_notif__)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
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
            name='RankList',
            fields=[
                ('rank_id', models.IntegerField(serialize=False, primary_key=True)),
                ('rank_name', models.CharField(max_length=100, null=True, blank=True)),
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
            name='ScholarShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('scolar_doc', models.FileField(default=b'null', upload_to=institute.models.__get_path_schdoc__)),
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
            name='SeminarsConf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100, null=True, verbose_name=b'description', blank=True)),
                ('doc', models.FileField(upload_to=institute.models.__get_path_seminars__)),
                ('date', models.CharField(max_length=20, null=True, blank=True)),
                ('time', models.CharField(max_length=10, null=True, blank=True)),
                ('venue', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tender_id', models.CharField(max_length=100, null=True, blank=True)),
                ('dept', models.CharField(max_length=100, null=True, verbose_name=b'Department', blank=True)),
                ('posting_dt', models.CharField(max_length=100, null=True, verbose_name=b'Posting date', blank=True)),
                ('closing_dt', models.CharField(max_length=100, null=True, verbose_name=b'Closing date', blank=True)),
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
    ]
