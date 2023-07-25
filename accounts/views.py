from django.shortcuts import render, redirect
from accounts import forms

def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.approve = False
            user.save()
            return redirect('accounts:sign-up-successful')
    else:
        form = forms.SignUpForm()

    return render(request, 'registration/sign-up.html', {'form': form})
    
def sign_up_successful(request):
    return render(request, 'registration/sign-up-successful.html')