from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import ActivityForm
from .models import Activity, Request

from datetime import date, datetime
from django.core.paginator import Paginator

def activities(request):
    page_number = request.GET.get('page')
    today= date.today()
    now = datetime.now()
    form = ActivityForm()
    user = request.user

    available_activities = Activity.objects.filter(available = True, start_datetime__gte=now).values()
    activities= available_activities.order_by('start_datetime')
    activities = Paginator(activities,3)
    future = activities.get_page(page_number)

    temp = available_activities.filter(start_datetime__date=today).values()
    temp = temp.order_by('start_datetime')
    temp = Paginator(temp, 2)
    featured = temp.get_page(page_number)

    context = {
        'date':today,
        'future':future,
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
