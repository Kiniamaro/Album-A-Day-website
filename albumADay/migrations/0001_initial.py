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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_name', models.CharField(max_length=200)),
                ('album_artist', models.CharField(max_length=500)),
                ('album_year', models.IntegerField()),
                ('ablum_comments', models.TextField()),
                ('album_cover', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='albumADay.Genre'),
            preserve_default=True,
        ),
    ]
