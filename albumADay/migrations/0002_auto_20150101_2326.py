# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumADay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_name',
            new_name='genre_Name',
        ),
    ]
