from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Group(models.Model):

    class GuestCount(models.TextChoices):
        GUEST1 = 'G1', _('Guest 1')
        GUEST2 = 'G2', _('Guest 2')
        GUEST3 = 'G3', _('Guest 3')
        GUEST4 = 'G4', _('Guest 4')
        GUEST5 = 'G5', _('Guest 5')
        GUEST6 = 'G6', _('Guest 6')

    guest_count = models.CharField(
        max_length=6,
        choices=GuestCount.choices,
        default=GuestCount.GUEST1,
    )

    def is_highcount(self):
        return self.year_in_school in {
            self.GuestCount.GUEST4,
            self.GuestCount.GUEST5,
        }

    def __str__(self):
        return self.name