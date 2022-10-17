from django import forms
from allauth.account.forms import SignupForm, LoginForm
from .models import UserProfile

class LoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        del self.fields['login'].widget.attrs['placeholder']
        del self.fields['password'].widget.attrs['placeholder']
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'input-wide'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input-wide'})

class SignUpForm(SignupForm):
    first_name = forms.CharField(max_length=155)
    last_name = forms.CharField(max_length=155)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        del self.fields['email'].widget.attrs['placeholder']
        del self.fields['password1'].widget.attrs['placeholder']
        del self.fields['password2'].widget.attrs['placeholder']

        self.fields['first_name'].widget.attrs.update({
            'class': 'required  input-wide',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'required input-wide',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'required input-wide',
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'required input-wide',
        })
        self.fields['account_type'].widget.attrs.update({
            'class': 'required input-wide',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'required input-wide',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'required input-wide',
        })

    def custom_signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        profile = UserProfile()
        profile.phone_number = self.cleaned_data['phone_number']
        profile.account_types = self.cleaned_data['account_type']
        profile.save()
        user.save()