# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170927_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(verbose_name='分享内容', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(verbose_name='分享人', max_length=200),
        ),
    ]
