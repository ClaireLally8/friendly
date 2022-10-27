from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities, name='activities'),
    path('new_activity/', views.create_activity, name='create_activity'),
]