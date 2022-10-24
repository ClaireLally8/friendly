from email.policy import default
import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'Activities'

    activity_id = models.CharField(max_length=32, null=False, editable=False)
    host = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=False, blank=False)
    date = models.DateField()
    start_time =models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=140, null=False, blank=False)
    available = models.BooleanField(default=True)
    
    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

class Request(models.Model):
    activity = models.ForeignKey(Activity, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    





