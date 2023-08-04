from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from classes.models import Class

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    class_relation = models.ManyToManyField(Class)
    
@receiver(post_save, sender=CustomUser)
def create_teacher(sender, instance, created, **kwargs):
    if created and instance.user_type == 'TEACHER':
        Teacher.objects.create(user=instance)