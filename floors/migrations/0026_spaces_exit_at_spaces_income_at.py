# Generated by Django 5.0.6 on 2024-07-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0025_remove_spaces_income_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaces',
            name='exit_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha salida'),
        ),
        migrations.AddField(
            model_name='spaces',
            name='income_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha ingreso'),
        ),
    ]
