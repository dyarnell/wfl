# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20151110_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
                ('entrant', models.ForeignKey(to='players.Player')),
                ('week', models.ForeignKey(to='players.Week')),
            ],
            options={
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.RemoveField(
            model_name='standings',
            name='player',
        ),
        migrations.RemoveField(
            model_name='standings',
            name='season',
        ),
        migrations.DeleteModel(
            name='Standings',
        ),
    ]
