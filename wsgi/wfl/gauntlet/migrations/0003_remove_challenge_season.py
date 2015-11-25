# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gauntlet', '0002_auto_20151109_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='season',
        ),
    ]
