# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_auto_20150602_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notif_id',
            field=models.CharField(max_length=30, unique=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='slug',
            field=models.SlugField(unique=True, editable=False),
        ),
    ]
