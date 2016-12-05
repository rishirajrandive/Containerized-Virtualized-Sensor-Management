# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 20:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=100)),
                ('station_name', models.CharField(max_length=400)),
                ('station_desc', models.CharField(max_length=800)),
                ('latitude', models.FloatField(max_length=10)),
                ('longitude', models.FloatField(max_length=10)),
                ('location', models.CharField(max_length=400)),
                ('active', models.BooleanField(default=True)),
                ('container_id', models.CharField(default='0', max_length=100)),
                ('sensorOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserSensorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.SensorDetail')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sensordetail',
            name='sensor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.SensorType'),
        ),
    ]
