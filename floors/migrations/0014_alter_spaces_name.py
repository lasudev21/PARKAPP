# Generated by Django 5.0.6 on 2024-07-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0013_spaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaces',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre'),
        ),
    ]
