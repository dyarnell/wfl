# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gauntlet', '0003_remove_challenge_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='week',
            field=models.OneToOneField(to='players.Week'),
        ),
    ]
