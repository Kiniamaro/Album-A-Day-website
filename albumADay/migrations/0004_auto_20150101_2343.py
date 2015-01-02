# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumADay', '0003_auto_20150101_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='albumADay.Genre'),
            preserve_default=True,
        ),
    ]
