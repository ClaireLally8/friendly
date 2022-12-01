from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import ActivityForm, RequestForm
from .models import Activity, Request

from .helpers import get_userprofile, get_usertype

from datetime import date, datetime
from django.core.paginator import Paginator


def activities(request):
    page_number = request.GET.get('page')
    today = date.today()
    now = datetime.now()
    form = ActivityForm()
    user = request.user
    account = get_usertype(request, user)

    available_activities = Activity.objects.filter(
        available=True, start_datetime__gte=now).values()
    activities = available_activities.order_by('start_datetime')
    activities = Paginator(activities, 3)
    future = activities.get_page(page_number)

    temp = available_activities.filter(start_datetime__date=today).values()
    temp = temp.order_by('start_datetime')
    temp = Paginator(temp, 2)
    featured = temp.get_page(page_number)

    context = {
        'date': today,
        'future': future,
        'form': form,
        'user': user,
        'featured': featured,
        'account': account
    }
    return render(request, 'activities/activities_overview.html', context)


def create_activity(request):
    account = get_usertype(request, request.user)
    if account.account_type == 'Volunteer':
        if request.method == "POST":
            form = ActivityForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                form.instance.host = request.user
                form.save()
                return redirect('activities')
        else:
            form = ActivityForm()
            context = {
                'form': form,
                'account':account,
            }
            return render(request, 'activities/new_listing.html', context)
    return render(request, 'errors/permission_denied.html')


def edit_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    account = get_usertype(request, request.user)
    if request.user == activity.host:
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
                'account': account,
            }
        return render(request, 'activities/edit_activity.html', context)
    return render(request, 'errors/permission_denied.html')


def delete_activity(request, id):
    account = get_usertype(request, request.user)
    activity = get_object_or_404(Activity, id=id)
    if request.user == activity.host:
        activity.delete()
        return redirect('activities')
    return render(request, 'errors/permission_denied.html')


def view_activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    logged_in_user = request.user
    profile = get_userprofile(request, logged_in_user)
    account_type = get_usertype(request, logged_in_user)
    form = RequestForm(instance=activity)
    context = {
        'logged_in_user': logged_in_user,
        'account': account_type,
        'activity': activity,
        'profile': profile,
        'form': form,
    }
    return render(request, 'activities/activity_detail.html', context)


def my_activities(request):
    account = get_usertype(request, request.user)
    if account.account_type == 'Volunteer':
        activities = Activity.objects.filter(host=request.user).values()
        activities = activities.order_by('start_datetime')
        context = {
            'activities': activities,
            'account' : account,
        }
        return render(request, 'activities/my_activities.html', context)
    return render(request, 'errors/permission_denied.html')

def request_activity(request, id):
    account = get_usertype(request, request.user)
    if account.account_type == 'Elderly Member':
        if request.method == "POST":
            form = RequestForm(data=request.POST)
            activity = get_object_or_404(Activity, id=id)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.activity = activity
                form.save()
            return redirect(reverse(view_activity, args=[
                        activity.id]))
        else:
            return render(request, 'errors/permission_denied.html')

def request_history(request):
    account = get_usertype(request, request.user)
    if account.account_type == 'Elderly Member':
        requests = Request.objects.filter(user=request.user).values()

        context = {
            'requests': requests,
            'account' : account,
        }
        return render(request, 'activities/request_history.html', context)



