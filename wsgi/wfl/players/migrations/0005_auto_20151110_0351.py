# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20151109_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.IntegerField(choices=[(0, b'Spring'), (1, b'Summer'), (2, b'Fall'), (3, b'Winter')]),
        ),
    ]
