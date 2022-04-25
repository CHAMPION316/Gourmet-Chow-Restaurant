# Generated by Django 3.2 on 2022-04-25 22:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reservations.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0003_rename_group_guest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20, null=True)),
                ('reservation_date_and_time', models.DateTimeField(blank=True, null=True, validators=[reservations.models.Booking.validate_date])),
                ('number_of_customers', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
                'unique_together': {('user', 'customer_name', 'reservation_date_and_time')},
            },
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]