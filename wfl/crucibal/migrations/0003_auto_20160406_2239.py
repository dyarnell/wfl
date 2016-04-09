# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crucibal', '0002_contest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rules',
            field=models.TextField(),
        ),
    ]
