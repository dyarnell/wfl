# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20151110_2316'),
        ('gauntlet', '0005_auto_20151110_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challenge', models.ForeignKey(to='gauntlet.Challenge')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
        ),
    ]
