# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20151110_2316'),
        ('gauntlet', '0006_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='BracketMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='participant',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='player',
        ),
        migrations.AddField(
            model_name='challenge',
            name='lineup_set',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='participants',
            field=models.ManyToManyField(to='players.Player', blank=True),
        ),
        migrations.DeleteModel(
            name='Participant',
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
