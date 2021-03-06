# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studtests', '0023_auto_20150412_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='edit_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 11, 54, 44, 725000), verbose_name=b'date edited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 11, 54, 44, 725000), verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='edit_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 11, 54, 44, 724000), verbose_name=b'date edited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 11, 54, 44, 724000), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
