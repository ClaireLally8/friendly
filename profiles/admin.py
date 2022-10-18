from django.contrib import admin

# Register your models here.
from .models import UserProfile, UserType

admin.site.register(UserProfile)
admin.site.register(UserType)