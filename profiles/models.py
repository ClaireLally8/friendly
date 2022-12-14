from django.db.models.signals import post_save

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from .helpers import COUNTY_CHOICES

ACCOUNT_TYPE = (
    ('Elderly Member', 'Elderly Member',),
    ('Volunteer', 'Volunteer'),
)


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile')
    image = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=False)
    postcode = models.CharField(max_length=500, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(
        choices=COUNTY_CHOICES,
        null=True,
        blank=True,
        max_length=200)
    bio = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.user.username


class UserType(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    account_type = models.CharField(
        choices=ACCOUNT_TYPE,
        max_length=200,
        null=False,
        blank=False)

    def __str__(self):
        return self.user.username
