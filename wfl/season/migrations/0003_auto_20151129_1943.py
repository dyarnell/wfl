# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0002_auto_20151128_2308'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set([('entrant', 'week')]),
        ),
    ]
