from datetime import date
from django import forms
from .models import Activity, Request

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
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_datetime'].input_formats = ['%Y-%m-%dT%H:%M']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('message',)
        labels = {
            'message': 'Message to the Poster'
        }