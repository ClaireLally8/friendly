from django import forms
from allauth.account.forms import SignupForm, LoginForm

class UserSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=155)
    last_name = forms.CharField(max_length=155)
    tel = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        del self.fields['password1']
        del self.fields['password2']

        self.fields['first_name'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'required',
        })
        self.fields['tel'].widget.attrs.update({
            'class': 'required',
        })

    def custom_signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.tel_number = self.cleaned_data['tel']
        user.save()

class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        del self.fields['login'].widget.attrs['placeholder']
        del self.fields['password'].widget.attrs['placeholder']
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'input-wide'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'input-wide'})