# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BracketMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineup_set', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('level', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='game',
            field=models.ForeignKey(to='gauntlet.VideoGame'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='participants',
            field=models.ManyToManyField(to='players.Player', blank=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='week',
            field=models.OneToOneField(to='players.Week'),
        ),
        migrations.AddField(
            model_name='bracketmatch',
            name='challenge',
            field=models.ForeignKey(to='gauntlet.Challenge'),
        ),
        migrations.AddField(
            model_name='bracketmatch',
            name='player1',
            field=models.ForeignKey(related_name='player1', blank=True, to='players.Player'),
        ),
        migrations.AddField(
            model_name='bracketmatch',
            name='player2',
            field=models.ForeignKey(related_name='player2', blank=True, to='players.Player'),
        ),
    ]
