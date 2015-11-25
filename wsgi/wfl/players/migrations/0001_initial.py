# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.CharField(max_length=6, choices=[(b'winter', b'Winter'), (b'spring', b'Spring'), (b'summer', b'Summer'), (b'fall', b'Fall')])),
                ('year', models.DateField()),
                ('players', models.ManyToManyField(to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
                ('player', models.ForeignKey(to='players.Player')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='standings',
            field=models.ForeignKey(to='players.Standings'),
        ),
    ]
