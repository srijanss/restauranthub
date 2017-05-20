# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField(verbose_name='event date')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(max_length=100)),
                ('offer_details', models.CharField(max_length=200)),
                ('offer_valid_date', models.DateField(verbose_name='offer valid upto date')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('opening_hours', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_type', models.CharField(max_length=100)),
                ('restaurant', models.ManyToManyField(to='restauranthub.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='offers',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restauranthub.Restaurant'),
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(to='restauranthub.Restaurant'),
        ),
        migrations.AddField(
            model_name='events',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restauranthub.Restaurant'),
        ),
        migrations.AddField(
            model_name='cuisine',
            name='restaurant',
            field=models.ManyToManyField(to='restauranthub.Restaurant'),
        ),
    ]