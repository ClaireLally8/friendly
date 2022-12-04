from datetime import date
from django import forms
from .models import Activity

from .widgets import DateTimePickerInput, TimePickerInput


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'start_datetime', 'end_time',
                  'location', 'town', 'description')
        labels = {
            'name': 'Activity Type',
            'start_datetime': 'Date & Time of Activity',
            'end_time': 'End Time',
            'location': 'County',
            'town': 'Town (optional)',
            'description': 'Description',
        }
        widgets = {
            'start_datetime': DateTimePickerInput(),
            'end_time': TimePickerInput(),
        }
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['start_datetime'].input_formats = ['%Y-%m-%dT%H:%M']
