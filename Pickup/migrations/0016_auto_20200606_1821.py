# Generated by Django 3.0.7 on 2020-06-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pickup', '0015_remove_pickup_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickup',
            old_name='antenna',
            new_name='Antenna',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='bodyCover',
            new_name='BodyCover',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='cdPlayer',
            new_name='CDPlayer',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='cigrateCharger',
            new_name='CarPerfume',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='clock',
            new_name='CigeretteCharger',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='dickyMat',
            new_name='Clock',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='jack',
            new_name='DickyMat',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='mats',
            new_name='Jack',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='perfume',
            new_name='Mats',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='odoMetervalue',
            new_name='OdoMeter',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='remote',
            new_name='Remote',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='serviceBook',
            new_name='ServiceBook',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='spareWheel',
            new_name='SpareWheel',
        ),
        migrations.RenameField(
            model_name='pickup',
            old_name='toolKit',
            new_name='ToolKit',
        ),
        migrations.RemoveField(
            model_name='pickup',
            name='fuelLevel',
        ),
        migrations.AddField(
            model_name='pickup',
            name='FuelLevel',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=('1', '1'), max_length=7, null=True),
        ),
    ]
