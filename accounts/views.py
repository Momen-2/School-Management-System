from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group
from accounts import forms, models

def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.approve = False
            user.save()
           
            if user.user_type == 'ADMIN':
                group = Group.objects.get_or_create(name='Admin')
                group[0].user_set.add(user)
            
            if user.user_type == 'TEACHER':
                group = Group.objects.get_or_create(name='Teacher')
                group[0].user_set.add(user)
           
            if user.user_type == 'STUDENT':
                group = Group.objects.get_or_create(name='Student')
                group[0].user_set.add(user)
            
            login(request, user)
            
            return redirect('accounts:sign-up-successful')
    else:
        form = forms.SignUpForm()

    return render(request, 'registration/sign-up.html', {'form': form})

def admin(user):
    return user.groups.filter(name='Admin').exists()

def teacher(user):
    return user.groups.filter(name='Teacher').exists()

def student(user):
    return user.groups.filter(name='Student').exists()

def sign_up_successful(request):
    if admin(request.user):
        approved = models.CustomUser.objects.all().filter(id=request.user.id, approve=True)
        
        if approved:
            return redirect('dashboards:admin-dashboard')
        else:
            return render(request,'accounts/wait-for-approve.html')
        
    elif teacher(request.user):
        approved = models.CustomUser.objects.all().filter(id=request.user.id, approve=True)
        
        if approved:
            return redirect('dashboards:teacher-dashboard')
        else:
            return render(request,'accounts/wait-for-approve.html')
        
    elif student(request.user):
        approved = models.CustomUser.objects.all().filter(id=request.user.id, approve=True)
        
        if approved:
            return redirect('dashboards:student-dashboard')
        else:
            return render(request,'accounts/wait-for-approve.html')
    
    messages.error(request, 'You are not authorized to access this page.')
    
    return redirect('home:home')