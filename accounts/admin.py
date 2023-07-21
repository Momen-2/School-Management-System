from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts import forms
from accounts import models

class MyUserAdmin(UserAdmin):
    form = forms.SignUpForm
    model = models.CustomUser
    list_display = ['username', 'mobile_number', 'birth_date']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('mobile_number', 'birth_date')}),)

admin.site.register(models.CustomUser, MyUserAdmin)