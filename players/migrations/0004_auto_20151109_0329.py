# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20151109_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.IntegerField()),
                ('season', models.ForeignKey(to='players.Season')),
            ],
        ),
        migrations.AlterModelOptions(
            name='standings',
            options={'verbose_name_plural': 'Standings'},
        ),
    ]
