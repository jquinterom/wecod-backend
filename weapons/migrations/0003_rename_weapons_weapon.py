# Generated by Django 4.2.4 on 2023-08-04 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0002_weapons_created_timestamp_weapons_updated_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weapons',
            new_name='Weapon',
        ),
    ]
