from django.db import models
from django.contrib.auth.models import User

from activities.models import Activity


class Request(models.Model):
    req_id = models.AutoField(primary_key=True)
    request_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    request_user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000, null=True, blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.req_id)
