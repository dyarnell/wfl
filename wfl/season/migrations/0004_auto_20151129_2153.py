# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0003_auto_20151129_1943'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='week',
            unique_together=set([('season', 'week')]),
        ),
    ]
