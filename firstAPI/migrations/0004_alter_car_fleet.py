# Generated by Django 4.0.3 on 2022-04-11 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstAPI', '0003_fleet_car_fleet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fleet',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstAPI.fleet'),
        ),
    ]
