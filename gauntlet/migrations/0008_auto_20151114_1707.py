# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gauntlet', '0007_auto_20151114_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='participants',
            field=models.ManyToManyField(to='players.Player', null=True),
        ),
    ]
