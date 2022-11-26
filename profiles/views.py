from django.shortcuts import render,get_object_or_404

from django.contrib.auth.models import User

from .models import UserProfile, UserType


def profile(request):
    user_tmp = request.user
    user = get_object_or_404(User, username=user_tmp)
    profile = UserProfile.objects.filter(user=user).values()
    user_type = UserType.objects.filter(user=user).values()

    context = {
        'user':user,
        'profile':profile,
        'user_type': user_type
    }
    return render(request, 'profiles/profile_overview.html', context)
