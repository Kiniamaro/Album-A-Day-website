# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('album_Name', models.CharField(max_length=200)),
                ('album_Artist', models.CharField(max_length=500)),
                ('album_year', models.IntegerField()),
                ('ablum_comments', models.TextField()),
                ('album_cover', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='AlbumGenre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('album', models.ForeignKey(to='albumADay.Album')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=200)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.AddField(
            model_name='albumgenre',
            name='genre',
            field=models.ForeignKey(to='albumADay.Genre'),
            preserve_default=True,
        ),
    ]
