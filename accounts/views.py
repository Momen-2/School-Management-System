from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from accounts import forms

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign-up.html'