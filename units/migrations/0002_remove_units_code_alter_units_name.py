# Generated by Django 4.0.2 on 2022-02-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='units',
            name='code',
        ),
        migrations.AlterField(
            model_name='units',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='code'),
        ),
    ]