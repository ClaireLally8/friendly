from profiles.models import UserProfile

def get_userprofile(request):
    profile = UserProfile.objects.filter(user=request.user)
    if profile.exists():
        return profile.first()
    return None