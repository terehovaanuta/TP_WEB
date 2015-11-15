# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_terehova_app', '0004_answer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.ForeignKey(to='ask_terehova_app.Answer')),
                ('user', models.ForeignKey(to='ask_terehova_app.Profile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(to='ask_terehova_app.Question')),
                ('user', models.ForeignKey(to='ask_terehova_app.Profile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('answer', models.ManyToManyField(to='ask_terehova_app.Answer')),
                ('question', models.ManyToManyField(to='ask_terehova_app.Question')),
            ],
        ),
    ]
