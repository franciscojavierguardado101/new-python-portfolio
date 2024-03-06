from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254,)
    username = forms.CharField(max_length=30, required=True,)

    class Meta:
        model = User 
        fields = ["username", "email", "password1"]

    def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            del self.fields['password2']
