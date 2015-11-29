# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='duration',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='week',
            name='kickoff',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
