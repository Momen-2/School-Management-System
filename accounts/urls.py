from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
]