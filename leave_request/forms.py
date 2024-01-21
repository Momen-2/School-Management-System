from django import forms
from leave_request import models

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = models.LeaveRequest
        fields = ["start_date", "end_date", "reason"]