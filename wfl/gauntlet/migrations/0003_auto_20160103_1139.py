# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gauntlet', '0002_auto_20160103_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='challenge',
            options={'ordering': ['-week']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='challenge',
            order_with_respect_to=None,
        ),
    ]
