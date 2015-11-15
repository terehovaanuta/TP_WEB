# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_terehova_app', '0003_answer_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='ask_terehova_app.Profile', null=True),
        ),
    ]
