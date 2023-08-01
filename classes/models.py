from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)
    academic_year = models.IntegerField(blank=True, null=True)
    grade_level = models.CharField(max_length=10, blank=True, null=True)
    section = models.CharField(max_length=10, blank=True, null=True)
    homeroom_teacher = models.CharField(max_length=100, blank=True, null=True)
    subject_combination = models.CharField(max_length=100, blank=True, null=True)
    class_capacity = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    class_schedule = models.CharField(max_length=255, blank=True, null=True)
    room_number = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name