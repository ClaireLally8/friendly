from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import RequestForm
from .models import Request

from activities.models import Activity
from activities.helpers import get_userprofile, get_usertype
from activities.views import view_activity


def request_activity(request, activity_id):
    account = get_usertype(request, request.user)
    if account.account_type == 'Elderly Member':
        if request.method == "POST":
            form = RequestForm(data=request.POST)
            activity = get_object_or_404(Activity, id=activity_id)
            requests = Request.objects.filter(
                request_activity=activity_id,
                request_user=request.user).values()
            if requests:
                return redirect(reverse(view_activity, args=[
                    activity.id]))
            else:
                if form.is_valid():
                    form.instance.request_activity = activity
                    form.instance.request_user = request.user
                    form.save()
                    return redirect(reverse(view_activity, args=[
                        activity.id]))
    else:
        return render(request, 'errors/permission_denied.html')


def request_history(request):
    account = get_usertype(request, request.user)
    if account.account_type == 'Elderly Member':
        activities = Activity.objects.filter()
        accepted = Request.objects.filter(
            request_user=request.user, accepted=True).values()
        pending = Request.objects.filter(
            request_user=request.user,
            accepted=False).values()
        context = {
            'activities': activities,
            'account': account,
            'accepted': accepted,
            'pending': pending,
        }
        return render(
            request,
            'activity_requests/request_history.html',
            context)


def cancel_request(request, req_id, id):
    req = get_object_or_404(Request, req_id=req_id)
    activity = get_object_or_404(Activity, id=id)
    if req:
        if req.accepted:
            cancel_accepted_request(request, activity, req)
        else:
            req.delete()
            return redirect(reverse(view_activity, args=[
            activity.id]))
    return render(request, 'errors/permission_denied.html')


def cancel_accepted_request(request, activity, req):
    activity.accepted = False
    req.delete()
    return redirect(reverse(view_activity, args=[
            activity.id]))


def accept_request(request, req_id, id):
    req = get_object_or_404(Request, req_id=req_id)
    activity = get_object_or_404(Activity, id=id)
    if activity.host.id == request.user.id:
        req.accepted = True
        req.save()
        activity.available = False
        activity.save()

        return redirect(reverse(view_activity, args=[
            activity.id]))
