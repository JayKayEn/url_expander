# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('short_url', models.URLField()),
                ('expanded_url', models.URLField()),
                ('status_code', models.CharField(max_length=3)),
                ('page_title', models.CharField(max_length=200)),
            ],
        ),
    ]
