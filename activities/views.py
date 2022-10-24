from django.shortcuts import render
from .forms import ActivityForm
# Create your views here.
def activities(request):
    form = ActivityForm()
    context = {
        'form': form
    }
    return render(request, 'activities/activities_overview.html', context)