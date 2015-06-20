# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0011_auto_20150613_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='hod_email',
        ),
        migrations.RemoveField(
            model_name='department',
            name='hod_name',
        ),
    ]
