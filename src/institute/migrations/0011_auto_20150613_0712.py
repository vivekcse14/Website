# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0010_auto_20150608_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phdresearch',
            name='sv_desgination',
        ),
        migrations.AlterField(
            model_name='headofdepartments',
            name='department',
            field=models.ForeignKey(to='institute.Department'),
        ),
        migrations.AlterField(
            model_name='headofdepartments',
            name='name',
            field=models.ForeignKey(to='institute.Faculty'),
        ),
    ]
