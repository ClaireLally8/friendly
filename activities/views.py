from django.shortcuts import render
from .forms import ActivityForm
from .models import Activity, Request

from datetime import date
# Create your views here.
def activities(request):
    form = ActivityForm()
    activities = Activity.objects.all()
    today= date.today()

    context = {
        'today':today,
        'form': form,
        'activities': activities
    }
    return render(request, 'activities/activities_overview.html', context)