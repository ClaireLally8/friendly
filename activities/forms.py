from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('host', 'name', 'date',
                  'start_time', 'end_time', 
                  'location', 'description')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Activity Type',
            'date': 'Date of Activity',
            'start_time': 'Start Time',
            'end_time': 'End Time',
            'location': 'Location',
            'description': 'Description',
            'host': 'Host',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False