# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='standings',
        ),
        migrations.AddField(
            model_name='standings',
            name='season',
            field=models.ForeignKey(default=1, to='players.Season'),
            preserve_default=False,
        ),
    ]
