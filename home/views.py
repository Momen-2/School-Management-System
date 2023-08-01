from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

def home(request):
    if request.user.is_authenticated and request.user.approve and Group.objects.filter(user=request.user).exists():
        return redirect('accounts:sign-up-successful')
    
    return render(request,'home/home.html')