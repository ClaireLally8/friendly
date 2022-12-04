from django.shortcuts import render, reverse, redirect, get_object_or_404

from activities.views import activities

def index(request):
    if request.user.is_authenticated:
        return redirect(activities)
    else:
        return render(request, 'main/index.html')
