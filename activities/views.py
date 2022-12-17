from django.shortcuts import render, reverse, redirect, get_object_or_404

from .forms import ActivityForm
from .models import Activity
from .helpers import get_userprofile, get_usertype, update_expired

from activity_requests.models import Request
from activity_requests.forms import RequestForm

from datetime import date, datetime
from django.core.paginator import Paginator


def activities(request):
    update_expired()
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
    host_profile = get_userprofile(request, activity.host)
    account_type = get_usertype(request, request.user)
    activity_requests = Request.objects.filter(request_activity=id)
    login_user_request = Request.objects.filter(request_user=request.user, request_activity=id)
    form = RequestForm()
    context = {
        'user_account': account_type,
        'account':account_type,
        'activity': activity,
        'host_profile': host_profile,
        'form': form,
        'activity_requests':activity_requests,
        'login_user_request': login_user_request,
       }
    return render(request, 'activities/activity_detail.html', context)


def my_activities(request):
    account = get_usertype(request, request.user)
    today = date.today()
    now = datetime.now()
    user = request.user
    if account.account_type == 'Volunteer':
        all_activities = Activity.objects.filter(host=user).values().order_by('start_datetime')
        today_activities = all_activities.filter(available=True, start_datetime__date=today, active=True).values()
        available_activities = all_activities.filter(available=True, active=True).values()
        accepted_activities = all_activities.filter(available=False, active=True).values()
        expired_activities = all_activities.filter(active=False).values()

        context = {
            'today_activities': today_activities,
            'available_activities': available_activities,
            'accepted_activities': accepted_activities,
            'expired_activities': expired_activities,
            'account' : account,
            'date': today,
            'user': user,
        }
        return render(request, 'activities/my_activities.html', context)
    return render(request, 'errors/permission_denied.html')
