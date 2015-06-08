# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_auto_20150601_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(default=b'theory', max_length=15, choices=[(b'practical', b'Practical'), (b'theory', b'Theory')]),
        ),
    ]
