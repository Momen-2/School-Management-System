from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts import models

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.CustomUser
        fields = ['username', 'mobile_number', 'birth_date']