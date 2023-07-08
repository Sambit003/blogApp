from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Comments, Subscribe
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'content', 'name', 'email', 'website'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Type your Comment'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['website'].widget.attrs['placeholder'] = 'Website'


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'email': _(''),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email ID'


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email ID'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("User already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("User already exists")
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']