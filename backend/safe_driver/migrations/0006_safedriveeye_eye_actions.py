# Generated by Django 2.2.17 on 2021-02-16 14:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0005_auto_20210216_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='safedriveeye',
            name='eye_actions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]