# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumADay', '0004_auto_20150101_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_Artist',
            new_name='album_artist',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_Name',
            new_name='album_name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genre_Name',
            new_name='genre_name',
        ),
    ]
