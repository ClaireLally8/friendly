from django.shortcuts import render,get_object_or_404

from django.contrib.auth.models import User

from .models import UserProfile, UserType


def profile(request):
    user_tmp = request.user
    user = get_object_or_404(User, username=user_tmp)
    profile = get_object_or_404(UserProfile, user=user)
    user_type = get_object_or_404(UserType, user=user)

    context = {
        'user':user,
        'profile':profile,
        'user_type': user_type
    }
    return render(request, 'profiles/profile_overview.html', context)
