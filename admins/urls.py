from django.urls import path
from admins import views

app_name = "admins"

urlpatterns = [
    path("admin-dashboard", views.AdminDashboardTemplateView.as_view(), name="dashboard"),
]