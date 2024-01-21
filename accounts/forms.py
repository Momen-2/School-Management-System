from django.contrib.auth.forms import UserCreationForm
from accounts import models

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.CustomUser
        fields = ["username", "first_name", "last_name","mobile_number", "user_type","gender", "profile_picture", "birthday_date"]