from django.db import models
from accounts.models import CustomUser

class Attendance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)