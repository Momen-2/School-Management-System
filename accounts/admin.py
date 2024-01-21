from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models

fields = list(UserAdmin.fieldsets)
fields[1] = ["Personal info", {"fields": ["first_name", "last_name","mobile_number", "user_type","gender", "profile_picture", "birthday_date"]}]
fields[2] = ["Permissions", {"fields": ["approved", "is_active", "is_staff", "is_superuser", "groups","user_permissions"]}]
UserAdmin.fieldsets = list(fields)

admin.site.register(models.CustomUser, UserAdmin)