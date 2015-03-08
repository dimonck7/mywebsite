# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_ver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ver',
            name='datetime',
        ),
        migrations.AddField(
            model_name='ver',
            name='content',
            field=models.TextField(default=1, max_length=10000),
            preserve_default=False,
        ),
    ]
