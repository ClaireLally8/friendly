from django.shortcuts import render
from django.core.paginator import Paginator

from .forms import ActivityForm
from .models import Activity, Request

from datetime import date
# Create your views here.
def activities(request):
    form = ActivityForm()
    activities = Activity.objects.all()
    today= date.today()
    paginator = Paginator(activities, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'today':today,
        'form': form,
    }
    return render(request, 'activities/activities_overview.html', context)