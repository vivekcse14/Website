# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_auto_20150602_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminofficial',
            name='email_off',
            field=models.EmailField(null=True, validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')], error_messages={b'invalid': b'Enter your Official Email-ID.'}, max_length=254, blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='email_off',
            field=models.EmailField(max_length=254, unique=True, error_messages={b'invalid': b'Enter your Official Email-ID.'}, validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')]),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='email_other',
            field=models.EmailField(default=None, max_length=254, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notif_id',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='quality',
            field=models.CharField(default=b'new', max_length=3),
        ),
        migrations.AlterField(
            model_name='notification',
            name='slug',
            field=models.SlugField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(to='institute.Department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, error_messages={b'invalid': b'Enter your Official Email-ID.'}, validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')]),
        ),
    ]
