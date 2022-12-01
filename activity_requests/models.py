from django.db import models
from django.contrib.auth.models import User

from activities.models import  Activity


class Request(models.Model):
    activity = models.ForeignKey(Activity,null=False,blank=False,on_delete=models.CASCADE,related_name="activity")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="request")
    message = models.TextField(max_length=1000, null=True, blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.activity.id)
