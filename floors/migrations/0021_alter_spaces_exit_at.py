# Generated by Django 5.0.6 on 2024-07-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0020_spaces_exit_at_spaces_income_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaces',
            name='exit_at',
            field=models.DateTimeField(blank=True, default='', verbose_name='Fecha salida'),
        ),
    ]
