# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gauntlet', '0004_auto_20151110_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='result',
            name='player',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
