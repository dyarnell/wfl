# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='players',
            field=models.ManyToManyField(to='players.Player', blank=True),
        ),
    ]
