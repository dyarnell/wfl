# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20151109_0329'),
        ('gauntlet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.IntegerField()),
                ('challenge', models.ForeignKey(to='gauntlet.Challenge')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
        ),
        migrations.AddField(
            model_name='videogame',
            name='level',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videogame',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='game',
            field=models.ForeignKey(to='gauntlet.VideoGame'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='season',
            field=models.ForeignKey(to='players.Season'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='week',
            field=models.ForeignKey(to='players.Week'),
        ),
    ]
