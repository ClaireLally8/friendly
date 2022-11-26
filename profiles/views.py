from django.shortcuts import render

from allauth import Users
from .models import UserProfile, UserType

def profile(request):
    user = request.user
    account = Users.objects.filter(username=user).values()
    profile = UserProfile.objects.filter(user=user).values()
    user_type = UserType.objects.filter(user=user).values()

    context = {
        'user':user,
        'profile':profile,
        'user_type': user_type
    }
    return render(request, 'profiles/profile_overview.html', context)
