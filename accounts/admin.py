from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts import forms
from accounts import models

fields = list(UserAdmin.fieldsets)
fields[1] = ['Personal info', {'fields': ['first_name', 'last_name','mobile_number', 'user_type','gender', 'profile_picture', 'birthday_date']}]
UserAdmin.fieldsets = list(fields)

admin.site.register(models.CustomUser, UserAdmin)