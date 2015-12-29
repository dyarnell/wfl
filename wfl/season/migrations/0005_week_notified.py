# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0004_auto_20151129_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
