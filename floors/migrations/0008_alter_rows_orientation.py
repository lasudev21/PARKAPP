# Generated by Django 5.0.6 on 2024-07-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0007_alter_rows_floor_alter_rows_numberparq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rows',
            name='orientation',
            field=models.CharField(choices=[('H', 'HORIZONTAL'), ('V', 'VERTICAL')], default='H', max_length=1),
        ),
    ]
