from django.db import models
from accounts.models import CustomUser
from classes.models import Class

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    class_relation = models.ManyToManyField(Class)