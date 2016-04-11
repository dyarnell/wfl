# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0009_season_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='week',
            name='location',
            field=models.ForeignKey(default=1, to='season.Location'),
            preserve_default=False,
        ),
    ]
