# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150818_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]
