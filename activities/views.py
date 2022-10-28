from cProfile import Profile
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .forms import ActivityForm
from .models import Activity, Request

from datetime import date
from .helpers import get_userprofile

def activities(request):
    form = ActivityForm()
    activities = Activity.objects.all()
    today= date.today()

    context = {
        'page_obj': activities,
        'today':today,
        'form': form,
    }
    return render(request, 'activities/activities_overview.html', context)

def create_activity(request):
    if request.method == "POST":
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            form.instance.host = request.user
            activity = form.save(commit=False)
            activity.save()
            return redirect('activities')
    else:
        form = ActivityForm()
        context = {
        'form': form,
    }
        return render(request, 'activities/new_listing.html', context)
