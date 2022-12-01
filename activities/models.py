import uuid
from django.db import models
from django.contrib.auth.models import User

from profiles.helpers import COUNTY_CHOICES


class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'Activities'

    id = models.AutoField(primary_key=True)
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=False, blank=False)
    start_datetime = models.DateTimeField()
    end_time = models.TimeField()
    location = models.CharField(
        choices=COUNTY_CHOICES,
        null=True,
        blank=True,
        max_length=200)
    town = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=140, null=False, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
