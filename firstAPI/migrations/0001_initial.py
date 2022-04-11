# Generated by Django 4.0.3 on 2022-04-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('rz', models.CharField(max_length=8)),
                ('vin', models.CharField(max_length=17)),
                ('power', models.IntegerField(null=True)),
            ],
        ),
    ]