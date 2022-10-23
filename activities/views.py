from django.shortcuts import render
# Create your views here.
def activities(request):
    return render(request, 'activities/activities_overview.html')