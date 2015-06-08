# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0007_auto_20150604_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='engg_year',
        ),
        migrations.AlterField(
            model_name='student',
            name='year_of_admission',
            field=models.IntegerField(default=0),
        ),
    ]
