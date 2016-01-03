# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gauntlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='challenge',
            order_with_respect_to='week',
        ),
    ]
