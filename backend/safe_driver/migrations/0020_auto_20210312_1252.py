# Generated by Django 2.2.19 on 2021-03-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0019_auto_20210311_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='btwbus',
            name='map_data',
            field=models.TextField(blank=True, null=True, verbose_name='Map Data'),
        ),
        migrations.AddField(
            model_name='btwclassa',
            name='map_data',
            field=models.TextField(blank=True, null=True, verbose_name='Map Data'),
        ),
        migrations.AddField(
            model_name='btwclassb',
            name='map_data',
            field=models.TextField(blank=True, null=True, verbose_name='Map Data'),
        ),
        migrations.AddField(
            model_name='btwclassc',
            name='map_data',
            field=models.TextField(blank=True, null=True, verbose_name='Map Data'),
        ),
    ]