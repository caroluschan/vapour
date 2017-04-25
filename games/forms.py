from django import forms
# from .models import UserAvatar
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class middleManAvatar(forms.Form):
	avatar_image = forms.FileField()
