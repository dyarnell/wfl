# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0008_auto_20160103_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
