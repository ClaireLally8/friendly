from django.db.models.signals import post_save

from django.conf import settings
from django.db import models

ACCOUNT_TYPE = (
    ('eld', 'Elderly Member'),
    ('vol', 'Volunteer'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    account_type = models.CharField(choices=ACCOUNT_TYPE,max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=30, null=False)
    postcode = models.CharField(max_length=500, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False)
    street_address1 = models.CharField(max_length=80, null=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.user.username

    

