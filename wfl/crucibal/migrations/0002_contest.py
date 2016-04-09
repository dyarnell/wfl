# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0009_season_completed'),
        ('crucibal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lineup_set', models.DateTimeField(null=True, blank=True)),
                ('game', models.ForeignKey(to='crucibal.Game')),
                ('participants', models.ManyToManyField(to='season.Player', blank=True)),
                ('week', models.OneToOneField(to='season.Week')),
            ],
            options={
                'ordering': ['week'],
            },
        ),
    ]
