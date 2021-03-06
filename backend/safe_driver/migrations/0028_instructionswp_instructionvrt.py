# Generated by Django 2.2.19 on 2021-04-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0027_auto_20210402_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructionSWP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.TextField()),
                ('field_name', models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=32, unique=True, verbose_name='Field Name')),
            ],
            options={
                'verbose_name': 'Instruction for SWP',
                'verbose_name_plural': 'Instructions for SWP',
                'ordering': ('field_name',),
            },
        ),
        migrations.CreateModel(
            name='InstructionVRT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.TextField()),
                ('field_name', models.CharField(default=None, help_text='Type/select field name underscore and without any space matched with db field', max_length=32, unique=True, verbose_name='Field Name')),
            ],
            options={
                'verbose_name': 'Instruction for VRT',
                'verbose_name_plural': 'Instructions for VRT',
                'ordering': ('field_name',),
            },
        ),
    ]
