from django import forms
from allauth.account.forms import SignupForm, LoginForm
from .models import UserProfile, UserType

ACCOUNT_TYPE = (
    ('eld', 'Elderly Member'),
    ('vol', 'Volunteer'),
)

class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        del self.fields['login'].widget.attrs['placeholder']
        del self.fields['password'].widget.attrs['placeholder']
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'input-wide'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input-wide'})

class UserSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=155)
    last_name = forms.CharField(max_length=155)
    phone_number = forms.CharField(max_length=30)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        
        del self.fields['email'].widget.attrs['placeholder']
        del self.fields['username'].widget.attrs['placeholder']
        del self.fields['password1'].widget.attrs['placeholder']
        del self.fields['password2'].widget.attrs['placeholder']

        self.fields['username'].widget.attrs.update({
            'class': 'required input-wide',
        })

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
        user.save()

        profile = UserProfile()
        userType = UserType()
        profile.user = user
        profile.phone_number = self.cleaned_data['phone_number']
        profile.save()
        userType.user = user
        userType.account_type = self.cleaned_data['account_type']
        userType.save()
        
        