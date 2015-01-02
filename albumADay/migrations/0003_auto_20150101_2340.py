# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumADay', '0002_auto_20150101_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumgenre',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumgenre',
            name='genre',
        ),
        migrations.AddField(
            model_name='genre',
            name='album',
            field=models.ManyToManyField(to='albumADay.Album'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='AlbumGenre',
        ),
    ]
