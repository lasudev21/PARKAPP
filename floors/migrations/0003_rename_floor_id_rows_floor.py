# Generated by Django 5.0.6 on 2024-07-04 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0002_rows'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rows',
            old_name='floor_id',
            new_name='floor',
        ),
    ]