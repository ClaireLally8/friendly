from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities, name='activities'),
    path('my-activities/', views.my_activities, name='my-activities'),
    path('<int:id>', views.view_activity, name='view-activity'),
    path('new/', views.create_activity, name='create-activity'),
    path('edit/<int:id>', views.edit_activity, name='edit-activity'),
    path('delete/<int:id>', views.delete_activity, name='delete-activity'),
]
