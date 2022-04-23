from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


# Create your models here.


class booking(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    booking_start=models.DateField()
