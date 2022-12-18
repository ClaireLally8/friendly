from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('message',)
        labels = {
            'message': 'Message to the Poster'
        }
