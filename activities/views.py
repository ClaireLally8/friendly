from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import ActivityForm
from .models import Activity, Request

from datetime import date
from django.core.paginator import Paginator

def activities(request):
    form = ActivityForm()
    activities = Activity.objects.all()
    today= date.today()
    temp = Activity.objects.filter(date=today).values()
    temp = temp.order_by('start_time')
    temp = Paginator(temp, 2)
    page_number = request.GET.get('page')
    featured = temp.get_page(page_number)
    user = request.user

    context = {
        'form': form,
        'user': user,
        'featured':featured
    }
    return render(request, 'activities/activities_overview.html', context)

def create_activity(request):
    if request.method == "POST":
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            form.instance.host = request.user
            form.save()
            return redirect('activities')
    else:
        form = ActivityForm()
        context = {
        'form': form,
    }
        return render(request, 'activities/new_listing.html', context)

def edit_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities')
    else:
        form = ActivityForm(instance=activity)
        context = {
        'form': form,
        'activity': activity,
    }
    return render(request, 'activities/edit_activity.html', context)

def delete_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    activity.delete()
    return redirect('activities')
