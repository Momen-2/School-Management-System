from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-up-successful/", views.sign_up_successful, name="sign-up-successful"),
]