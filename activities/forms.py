from datetime import date
from django import forms
from .models import Activity

from .widgets import DatePickerInput, TimePickerInput

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'date',
                  'start_time', 'end_time', 
                  'location', 'description')
        labels = {
            'name': 'Activity Type',
            'date': 'Date of Activity',
            'start_time': 'Start Time',
            'end_time': 'End Time',
            'location': 'Location',
            'description': 'Description',
        }
        widgets = {
            'date' : DatePickerInput(),
            'start_time' : TimePickerInput(),
            'end_time' : TimePickerInput(),

        }
