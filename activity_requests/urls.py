from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.request_activity, name='request-activity'),
    path('history/', views.request_history, name='request-history'),
]