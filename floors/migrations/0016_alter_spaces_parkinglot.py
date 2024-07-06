# Generated by Django 5.0.6 on 2024-07-05 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0015_spaces_parkinglot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaces',
            name='parkinglot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floors.parkinglots', verbose_name='Estacionamiento'),
        ),
    ]
