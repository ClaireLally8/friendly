from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import  RequestForm
from .models import Request

from activities.models import Activity
from activities.helpers import get_userprofile, get_usertype
from activities.views import view_activity



def request_activity(request, id):
    account = get_usertype(request, request.user)
    if account.account_type == 'Elderly Member':
        if request.method == "POST":
            form = RequestForm(data=request.POST)
            activity = get_object_or_404(Activity, id=id)
            requests = Request.objects.filter(activity_id=activity.id, user=request.user).values()
            if requests:
                return redirect(reverse(view_activity, args=[
                            activity.id]))
            else:
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
        activities = Activity.objects.prefetch_related('activity')
        accepted = Request.objects.filter(user=request.user, accepted=True).values()
        pending = Request.objects.filter(user=request.user, accepted=False).values()
        context = {
            'activities':activities,
            'account' : account,
            'accepted':accepted,
            'pending':pending,
        }
        return render(request, 'activity_requests/request_history.html', context)
   


