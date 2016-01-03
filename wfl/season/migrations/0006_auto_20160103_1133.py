# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0005_week_notified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['-season']},
        ),
    ]
