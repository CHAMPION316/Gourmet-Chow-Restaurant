# Generated by Django 3.2 on 2022-04-21 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='year_in_school',
            new_name='guest_count',
        ),
    ]
