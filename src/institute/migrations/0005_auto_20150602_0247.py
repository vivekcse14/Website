# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0004_auto_20150602_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='faculty_id',
            field=models.CharField(unique=True, max_length=100, editable=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, editable=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.CharField(max_length=2),
        ),
    ]
