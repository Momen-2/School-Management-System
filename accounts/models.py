from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile_number = models.IntegerField()
    birth_date = models.DateField()