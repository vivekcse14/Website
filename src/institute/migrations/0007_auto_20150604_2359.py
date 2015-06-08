# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0006_auto_20150603_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='engg_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='contact_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default=b'null', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.IntegerField(default=1, choices=[(2, b'Practical'), (1, b'Theory')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='quality',
            field=models.IntegerField(default=1, choices=[(1, b'new'), (0, b'old')]),
        ),
    ]
