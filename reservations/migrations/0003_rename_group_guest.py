# Generated by Django 3.2 on 2022-04-21 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_rename_year_in_school_group_guest_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Guest',
        ),
    ]
