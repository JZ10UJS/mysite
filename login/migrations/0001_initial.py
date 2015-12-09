# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=64, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=32, verbose_name='\u5bc6\u7801')),
            ],
        ),
    ]
