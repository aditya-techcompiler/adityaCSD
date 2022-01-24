# Generated by Django 2.2.19 on 2021-07-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0052_pretripcargoareabus_pretripinterioroperationbus_pretriprampbus'),
    ]

    operations = [
        migrations.AddField(
            model_name='vrtbacking',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtcoupling',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtdrivinghabits',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtengineoperations',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtparking',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtposttrip',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtpretrip',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtstartengine',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtuncoupling',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtuseclutch',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtuseofbrakes',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AddField(
            model_name='vrtuseoftransmission',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=0, verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='vrtbacking',
            name='does_not_hit_dock',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Doesn’t Hit Dock'),
        ),
        migrations.AlterField(
            model_name='vrtcoupling',
            name='raise_landing_gear',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Raise Landing Gear'),
        ),
        migrations.AlterField(
            model_name='vrtdrivinghabits',
            name='defensive_driving',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Defensive Driving'),
        ),
        migrations.AlterField(
            model_name='vrtengineoperations',
            name='check_gauges',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Checks Gauges'),
        ),
        migrations.AlterField(
            model_name='vrtparking',
            name='engine_off_pull_key',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Engine Off - Pull Key'),
        ),
        migrations.AlterField(
            model_name='vrtposttrip',
            name='leaks',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Leaks'),
        ),
        migrations.AlterField(
            model_name='vrtpretrip',
            name='serv_brake_test',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Serv Brake Test'),
        ),
        migrations.AlterField(
            model_name='vrtstartengine',
            name='seat_belt',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Seat Belt'),
        ),
        migrations.AlterField(
            model_name='vrtuncoupling',
            name='verify_firm_to_ground',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Verify Firm to Ground'),
        ),
        migrations.AlterField(
            model_name='vrtuseclutch',
            name='coast',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Coast'),
        ),
        migrations.AlterField(
            model_name='vrtuseofbrakes',
            name='hv_when_stopped_traffic',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='H/V when Stopped Traffic'),
        ),
        migrations.AlterField(
            model_name='vrtuseoftransmission',
            name='timing_down',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (0, 'N/A')], default=1, verbose_name='Timing Down'),
        ),
    ]