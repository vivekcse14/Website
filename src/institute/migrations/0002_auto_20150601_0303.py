# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='s_no',
        ),
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(default=b'null', max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(),
        ),
    ]
