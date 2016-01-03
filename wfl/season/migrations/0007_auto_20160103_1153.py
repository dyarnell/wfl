# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0006_auto_20160103_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['-week']},
        ),
    ]
