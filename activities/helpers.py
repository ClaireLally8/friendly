from profiles.models import UserProfile, UserType
from .models import Activity

from datetime import date, datetime


def get_userprofile(request, user):
    profile = UserProfile.objects.filter(user=user)
    if profile.exists():
        return profile.first()
    return None


def get_usertype(request, user):
    account = UserType.objects.filter(user=user)
    if account.exists():
        return account.first()
    return None


def update_expired():
    now = datetime.now()
    Activity.objects.filter(start_datetime__lte=now).update(active=False)
