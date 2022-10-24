from django.shortcuts import render
from .forms import ActivityForm
from .models import Activity, Request
# Create your views here.
def activities(request):
    form = ActivityForm()
    activities = Activity.objects.all()

    context = {
        'form': form,
        'activities': activities
    }
    return render(request, 'activities/activities_overview.html', context)