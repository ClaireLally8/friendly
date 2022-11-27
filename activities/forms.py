from datetime import date
from django import forms
from .models import Activity

from .widgets import DateTimePickerInput, TimePickerInput

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'start_datetime', 'end_time', 
                  'location', 'description')
        labels = {
            'name': 'Activity Type',
            'start_datetime': 'Date & Time of Activity',
            'end_time': 'End Time',
            'location': 'Location',
            'description': 'Description',
        }
        widgets = {
            'start_datetime' : DateTimePickerInput(),
            'end_time' : TimePickerInput(),

        }
