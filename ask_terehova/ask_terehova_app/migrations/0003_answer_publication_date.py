# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ask_terehova_app', '0002_question_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
