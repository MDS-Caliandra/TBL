# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-25 20:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0019_auto_20180124_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(choices=[('iRAT', 'iRAT'), ('gRAT', 'gRAT'), ('Exercise', 'Exercise')], default='Exercise', max_length=10)),
                ('score', models.PositiveIntegerField(default=0, help_text='Question score answered.', verbose_name='Score')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date that the submission of question is created.', verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Submissions',
                'ordering': ['user', 'exam', 'question', 'created_at'],
                'verbose_name': 'Submission',
            },
        ),
        migrations.RemoveField(
            model_name='alternative',
            name='score',
        ),
        migrations.RemoveField(
            model_name='question',
            name='score',
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exam.iRAT'),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Intermediary', 'Intermediary'), ('Advanced', 'Advanced')], default='basic', help_text='Difficulty level', max_length=15, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='question',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='TBLSessions.TBLSession'),
        ),
        migrations.AddField(
            model_name='submission',
            name='alternative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='questions.Alternative', verbose_name='Alternatives'),
        ),
        migrations.AddField(
            model_name='submission',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='questions.Question', verbose_name='Questions'),
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
    ]