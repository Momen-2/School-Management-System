from django.db import models
from courses.models import Course

class Subject(models.Model):
    subject_name = models.CharField(max_length=255, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject_name