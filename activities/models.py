import uuid
from django.db import models
from django.conf import settings

from profiles.models import UserProfile

from datetime import datetime, date

# Create your models here.
class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'Activities'

    activity_id = models.AutoField(primary_key=True)
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=False, blank=False)
    date = models.DateField()
    start_time =models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=140, null=False, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.activity_id)

class Request(models.Model):
    activity = models.ForeignKey(Activity, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.activity.activity_id)





