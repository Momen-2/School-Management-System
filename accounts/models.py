from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    GENDER_CHOICES = [('MALE', 'Male'), ('FEMALE', 'Female')]
    USER_TYPES = [('ADMIN', 'Admin'), ('TEACHER', 'Teacher'), ('STUDENT', 'Student')]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='MALE')
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='STUDENT')
    mobile_number = PhoneNumberField()
    profile_picture = models.ImageField(upload_to='profile-pictures/', blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True, help_text='yyyy-mm-dd')
    approve = models.BooleanField(default=False)