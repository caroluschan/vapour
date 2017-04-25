from django import forms
# from .models import UserAvatar
from django.contrib.auth.models import User
from .models import UserAvatar

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class middleManAvatar(forms.ModelForm):
	class Meta:
		model = UserAvatar
		fields = ['username', 'avatar']
