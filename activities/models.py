import uuid
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from profiles.models import UserProfile

from datetime import datetime, date

from profiles.helpers import COUNTY_CHOICES

class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'Activities'

    id = models.AutoField(primary_key=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activity")
    name = models.CharField(max_length=254, null=False, blank=False)
    start_datetime = models.DateTimeField()
    end_time = models.TimeField()
    location = models.CharField(choices=COUNTY_CHOICES, null=True, blank=True,max_length=200)
    town = models.CharField(max_length=200, null=True, blank = True)
    description = models.CharField(max_length=140, null=False, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class Request(models.Model):
    activity = models.ForeignKey(Activity, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.activity.id)





