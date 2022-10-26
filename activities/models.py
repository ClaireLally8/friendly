import uuid
from django.db import models
from django.conf import settings

from profiles.models import UserProfile

from datetime import datetime, date

# Create your models here.
class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'Activities'

    activity_id = models.CharField(max_length=32, null=False, editable=False)
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=False, blank=False)
    date = models.DateField()
    start_time =models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField(blank=True, null=True)
    location = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=140, null=False, blank=False)
    available = models.BooleanField(default=True)
    
    def _generate_activity_id(self):
        return uuid.uuid4().hex.upper()

    def _generate_activity_duration(self):
        return datetime.combine(date.today(), self.end_time) - datetime.combine(date.today(), self.start_time)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the activity ID and 
        activity duration if it hasn't been set already.
        """
        if not self.activity_id:
            self.activity_id = self._generate_activity_id()
        super().save(*args, **kwargs)

        if not self.duration:
            self.duration = self._generate_activity_duration()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.activity_id

class Request(models.Model):
    activity = models.ForeignKey(Activity, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.activity.activity_id





