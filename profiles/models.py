from django.db.models.signals import post_save

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

ACCOUNT_TYPE = (
    ('eld', 'Elderly Member'),
    ('vol', 'Volunteer'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=30, null=False)
    postcode = models.CharField(max_length=500, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.user.username

class UserType(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    account_type = models.CharField(choices=ACCOUNT_TYPE,max_length=200, null=False, blank=False)

    def __str__(self):
        return self.user.username

    

