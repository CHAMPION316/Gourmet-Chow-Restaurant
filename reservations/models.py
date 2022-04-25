from django.db import models



class Booking(models.Model):
    """
    Class for booking model
    in database and for booking form.
    """
    user = models.ForeignKey(User, null=True, blank=True)
    customer_name = models.CharField(max_length=20, null=True)
    reservation_date_and_time = models.DateTimeField(null=True)
                             