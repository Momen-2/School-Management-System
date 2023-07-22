from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts import forms
from accounts import models

class CustomUserAdmin(UserAdmin):
    add_form = forms.SignUpForm
    model = models.CustomUser
    list_display = ['username', 'first_name', 'last_name','mobile_number', 'gender', 'mobile_number', 'profile_picture', 'birthday_date']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('mobile_number',)}),)

admin.site.register(models.CustomUser, CustomUserAdmin)