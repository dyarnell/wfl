# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0007_auto_20160103_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['week']},
        ),
    ]
