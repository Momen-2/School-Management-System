from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from leave_request import forms
from leave_request import models

@login_required
def submit_leave_request(request):
    if request.method == "POST":
        form = forms.LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.user = request.user
            leave_request.save()
            return redirect("home:home")
    else:
        form = forms.LeaveRequestForm()
    return render(request, "leave_request/submit-leave.html", {"form": form})

@login_required
def leave_request_detail(request, request_id):
    leave_request = get_object_or_404(models.LeaveRequest, id=request_id)

    return render(request, "leave_request/leave-request-detail.html", {"leave_request": leave_request})
