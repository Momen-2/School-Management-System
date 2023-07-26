from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated and request.user.approve:
        return redirect('accounts:sign-up-successful') # redirect to user dashboard
    return render(request,'home/home.html')