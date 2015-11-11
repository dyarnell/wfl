# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 11, 9, 2, 38, 40, 941710, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
