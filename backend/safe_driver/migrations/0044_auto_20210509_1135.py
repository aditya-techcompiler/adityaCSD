# Generated by Django 2.2.19 on 2021-05-09 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0043_btwgeneralsafetyanddotadherencebus_btwhillsbus_btwinternalenvironmentbus_btwintersectionsbus_btwpark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btwinternalenvironmentbus',
            name='btw',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='btw_internal_environment_bus', to='safe_driver.BTWBus'),
        ),
    ]
